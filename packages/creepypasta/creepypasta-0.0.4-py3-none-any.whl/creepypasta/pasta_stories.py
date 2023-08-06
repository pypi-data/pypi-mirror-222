import json
import os
import re
import requests

from bs4 import BeautifulSoup
from datetime import date, datetime
import lxml.html
import pandas as pd
from pathlib import Path
from time import sleep
from tqdm import tqdm


def get_stories_from_listings_dirpath(dir_path="./list-pages/"):
    # get list of story links from path to directory with listings scraped 
    # from https://www.creepypasta.com/archive/?_orderby=date
    # example stories_list_fpath returned: './parsed-listings/2023-07-25_story_links.json'
    stories_list_fpath = StoryListingsParser.output_json(dir_path)

    # load json created above
    stories_list_dict = CreepyPastaGetter.get_stories_list_dict(stories_list_fpath)

    # for each listings file, get/fetch individual stories
    # TODO: returns a path to stories (currently returns none)
    for k in stories_list_dict.keys():
        CreepyPastaGetter.fetch_pasta_pages(k, stories_list_dict[k])
        # break after one round if test
        # break

    # stories_path to directory with individual story pages
    # returns list of dicts, one dict per story
    stories_path = "./story-pages/"
    all_stories_dict_list = CreepyPastaSoupParser.get_all_stories(stories_path)
    return all_stories_dict_list


class StoryListingsParser:
    """
    Container for methods parsing list-pages.
    """
    @classmethod
    def parse_listings_get_story_links_per_page(cls, listing_fpath):
        """
        Get list of links per listing_fpath

        listing_fpath: fpath to page_source from 
        https://www.creepypasta.com/archive/?_orderby=date
        example input:
        ./list-pages/2023-07-22__orderby=date&_page=29.html
        
        returns: list of links
        """
        file = open(listing_fpath, "r")
        page_html = file.read()
        file.close()

        soup = BeautifulSoup(page_html, "lxml")
        soup.title
        story_tags = soup.select("a.pt-cv-readmore")

        return [a["href"] for a in story_tags]
    
    @classmethod
    def get_all_story_links(cls, dir_path):        
        """
        Gets all files in dirpath directory and
        returns json-ready dict with story links by list page.
        
        dir_path: directory where multiple page_source files from
        https://www.creepypasta.com/archive/?_orderby=date

        example input:
        dir_path = "./list-pages/"

        ./list-pages/ dir contains:
        - '2023-07-22__orderby=date&_page=29.html'
        - '2023-07-22__orderby=date&_page=91.html'

        returns: json of all story links in a dict format
        example output:
        {{'2023-07-22__orderby=date&_page=29.html': 
            ['https://www.creepypasta.com/the-scariest-story-ever/',
             'https://www.creepypasta.com/windows-and-notes/'],
        '2023-07-22__orderby=date&_page=91.html': 
            ['https://www.creepypasta.com/three-friends-diner/',
             'https://www.creepypasta.com/written-in-the-stars/',
             'https://www.creepypasta.com/monster-painter/',
             'https://www.creepypasta.com/a-moment-of-horror/']}} 
        """
        
        # Get all files in listings directory
        files_list = PageFetcherUtils.get_all_files(dir_path)
        
        all_story_links = {}

        for fpath in files_list:
            if fpath == ".DS_Store":
                continue
            all_story_links[fpath] = cls.parse_listings_get_story_links_per_page(f"{dir_path}{fpath}")

        return all_story_links
    
    @classmethod
    def write_json_of_story_links_dicts(cls, dir_path):
        """
        Gets all story links using `get_all_story_links`.
        Creates JSON file using `output_json`.
        
        dir_path: directory where multiple page_source files from
        https://www.creepypasta.com/archive/?_orderby=date

        example input:
        dir_path = "./list-pages/
        
        writes: json w/ get_all_story_links output (story links per page dicts)
        returns: name of new json filepath    
        """
        with open(f"./parsed-listings/{date.today()}_story_links.json", "w") as outfile:
            story_links_dict = cls.get_all_story_links(dir_path)
            json.dump(story_links_dict, outfile, sort_keys=True)
            return outfile.name

    @classmethod
    def output_json(cls, dir_path):
        # returns: name of new json filepath to use with CreepyPastaGetter
        # this is just a convenience function for the module
        return cls.write_json_of_story_links_dicts(dir_path)


class PageFetcherUtils:
    """
    General utils non-specific to Creepypasta.
    """
    @classmethod
    def fetch_page(cls, url):
        """
        Needed to get ratings/reviews that are live-loaded on site.
        """
        ident = (
        # replace with info
        "Stephanie Andrews (jellomoat@gmail.com), " + 
        "scraping for educational purposes"
        )
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }

        print(f"Fetching {url}")
        return requests.get(
            url,
            headers=headers
        )
    
    @classmethod
    def get_html(cls, fpath):
        """
        Opens and reads file to HTML.
        
        `fpath`: path to file with saved `page_source`
        """
        file = open(fpath, "r")
        page_html = file.read()
        file.close()
        return page_html

    @classmethod
    def get_all_files(cls, dir_path, debug=False):
        """
        Lists all files in specified directory.
        
        `dir_path`: path to target directory
        """
        dir_list = os.listdir(dir_path)

        if debug:
            print("Files and directories in '", path, "' :")
            print(dir_list)
        return dir_list


class CreepyPastaGetter:
    """
    Gets/fetches stories from site.
    """
    @classmethod
    def get_stories_list_dict(cls, stories_list_fpath):
        """
        Opens and loads JSON file to dict.
        
        `stories_list_fpath`: path to JSON file
        """
        
        with open(stories_list_fpath, "r") as stories_list_file:
            return json.load(stories_list_file)
    
    @classmethod
    def fetch_pasta_pages(cls, list_page, links_list):
        """
        Using a list of links, finds/fetches story pages and writes to disk.
        Logs fetching history using `story_writing_log`.

        `list_page`: specific page # of the Creepypasta site archive
        `links_list`: links on that page to retrieve
        """
        # fetch each page
        for link in links_list:
            dest = Path("story-pages/" + f"published_stories_{link.split('/')[-2]}.html")
            if dest.exists(): # load it from file
                print(f"Already have {dest}, loading!")
                file = open(dest, "r")
                page_html = file.read()
                file.close()
            else: # fetch it!
                page_resp = PageFetcherUtils.fetch_page(link)
                page_html = page_resp.text
                sleep(2)

                # save to file
                with open(dest, "w") as f:
                    f.write(page_html)
                cls.story_writing_log(listing_fname=list_page, dest_fname=dest)

        return None

    @classmethod
    def error_writing_log(cls, exception, listing_fname="testing", dest_fname="testing", logname="error_log"):
        with open(f"{date.today()}_{logname}.txt", "a") as f:
            f.write(f"{listing_fname}, {dest_fname}\n")

    @classmethod
    def story_writing_log(cls, listing_fname="testing", dest_fname="testing", logname="stories_log"):
        with open(f"{date.today()}_{logname}.txt", "a") as f:
            f.write(f"{listing_fname}, {dest_fname}\n")


class CreepyPastaSoupParser:
    """
    Methods for parsing individual stories and all stories.
    """
    def __init__(self, fpath_or_link, is_fpath=True):
        self.fpath_or_link = fpath_or_link
        self.soup = self.get_soup(is_fpath)
        self.title = self.soup.title.string

    def get_soup(self, is_fpath):
        if is_fpath:
            page_html = PageFetcherUtils.get_html(self.fpath_or_link)
        else:
            page_html = PageFetcherUtils.fetch_page(self.fpath_or_link).text
        return BeautifulSoup(page_html, "lxml")
        
    def parse_story(self):
        parsed_story_dict = {}
        parsed_story_dict["title"] = self.title
        parsed_story_dict["link"] = self.story_link
        parsed_story_dict["date_str"] = self.published_date
        parsed_story_dict["story_text"], parsed_story_dict["author_str"] = self.__get_story_and_author_content()
        parsed_story_dict["reading_time_min"] = self.reading_time_min
        parsed_story_dict["story_cats"] = self.soup.find_all(self.__get_categories)
        parsed_story_dict["story_tags"] = self.soup.find_all(self.__get_tags)
        parsed_story_dict["story_uuid"] = self.story_uuid
        parsed_story_dict["story_rating"], parsed_story_dict["story_votes"] = self.__class__.get_ratings_and_votes(self.story_uuid)
        return parsed_story_dict

    @property
    def story_link(self):
        return self.soup.find("link", {"rel": "canonical"})["href"]

    @property
    def story_uuid(self):
        return self.soup.select_one("article")["id"].strip("post-")

    @property
    def published_date(self):
        raw_date = self.soup.select_one("span.published").string.strip(" ")
        date_str = datetime.strftime(datetime.strptime(raw_date, "%B %d, %Y"), "%Y-%m-%d")
        return date_str

    @property
    def reading_time_min(self):
        reading_time_el = self.soup.select_one("span.rt-reading-time")
        reading_time_raw_unit = reading_time_el.select_one("span.rt-postfix").string
        reading_time_raw_unit

        reading_time_raw = reading_time_el.select_one("span.rt-time").string.strip(" ")
        if (re.search(r"\D", reading_time_raw)):
            return 0.5 # stand-in for < 1 min
        reading_time_min = int(reading_time_raw) if re.search(r"minutes*", reading_time_raw_unit) else int(reading_time_raw * 60)
        return reading_time_min

    @property
    def story_content(self):
        return self.__get_story_and_author_content()[0]
    
    @property
    def author_content(self):
        return self.__get_story_and_author_content()[1]

    def __get_story_and_author_content(self):
        entry_content = self.soup.select('div.entry-content > p')
        if (len(entry_content) > 1) and hasattr(entry_content[-1], "text"):
            if "credit" in entry_content[-1].text.lower():
                story_content, author_str = entry_content[:-1], entry_content[-1].text
            else:
                story_content, author_str = entry_content, None
        else:
            if (len(entry_content) > 1) and "credit" in entry_content[-1].string.lower():
                story_content, author_str = entry_content[:-1], entry_content[-1].string
            else:
                story_content, author_str = entry_content, None  

        story_content = [(re.sub("<p>", "", p.text)) for p in story_content]

        if author_str:
            new_raw_author_regex = r"Credit[ed]*\s*[to]*\s*:*\s*([\w\s.]*\d*)\.*"
            wiki_user_author_regex = r"User:([a-z0-9]*)"
#             combined_regex = r"User:([a-z0-9]*)|Credit[ed]*\s*[to]*\s*:*\s*([\w\s.]*\d*)\.*"
            author_str_1 = re.search(
                new_raw_author_regex,
                author_str,
                re.IGNORECASE)
            author_str_2 = re.search(
                wiki_user_author_regex,
                author_str,
                re.IGNORECASE)
            author_str = author_str_1 or author_str_2
            author_str = author_str.group(1)
        return story_content, author_str

    def __get_categories(self, tag):
        return tag.has_attr('href') \
            and re.search(r"category", tag["href"]) \
            and not re.search(r"archive", tag["href"])

    def __get_tags(self, tag):
        return tag.has_attr('href') \
            and re.search(r"tag", tag["href"]) \
            and not re.search(r"instagram", tag["href"])

    ### BeautifulSoup for Ratings and Reviews
    ### NEED TO USE UNDOC API
    @classmethod
    def get_ratings_and_votes(cls, story_uuid):
        request_args = {
            "headers": {
                'authority': 'www.creepypasta.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.creepypasta.com',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            },
            "params": {
                'action': 'gdrts_live_handler',
            }
        }
    
        response = requests.post(
            'https://www.creepypasta.com/wp-admin/admin-ajax.php',
            params=request_args["params"],
            headers=request_args["headers"],
            data=cls.__get_data_arg(story_uuid),
        )

        rating_regex_2 = r"<strong>([0-9\.]*)<\/strong>\/10\.*\s*From\s*([0-9]*.*[0-9]*K*)\s*votes."
        rating_render_text = response.json()["items"][0]["render"]
        rating_groups = re.search(rating_regex_2, rating_render_text, flags=re.IGNORECASE)
        avg_rating, num_votes = rating_groups.group(1).strip(), rating_groups.group(2).strip()
        if "k" in num_votes.lower():
            num_votes_groups = re.search(r"([0-9]*\.*[0-9]*)\S*\s*K", num_votes, flags=re.IGNORECASE)
            num_votes = int(float(num_votes_groups.group(1)) * 1000) if num_votes_groups else num_votes

        print(f"avg rating: {avg_rating}/10, num votes: {num_votes}")

        return avg_rating, str(num_votes).strip()

    @classmethod
    def __get_data_arg(cls, story_id):
        data = {
            'req': '{"todo":"dynamic","items":[{"args":{"echo":false,"entity":"posts","name":"post","item_id":0,"id":' 
                + str(story_id) 
                + ',"method":"stars-rating","series":null},"method":{"votes_count_compact_show":true,"votes_count_compact_decimals":"2","cta":"","distribution":"normalized","rating":"average","style_name":"star", "labels":[]},"did":1},{"args":{"echo":false,"entity":"posts","name":"post","item_id":null,"id":' + str(story_id) + ',"method":"stars-rating","series":null,"disable_dynamic_load":false,"dynamic":true},"method":{"votes_count_compact_show":true,"votes_count_compact_decimals":"2","cta":"","distribution":"normalized","rating":"average","labels":[]},"did":2}]}'
        }
        return data
    
    @classmethod
    def get_all_stories(cls, stories_path = "./story-pages/"):
        # stories_path (default): './story-pages/' from CreepyPastaGetter
        stories_dicts = []
        parsed_count = 0
        error_count = 0
        for fpath in tqdm(PageFetcherUtils.get_all_files(stories_path)):
            if fpath == ".DS_Store":
                continue
            try:
                stories_dicts.append(CreepyPastaSoupParser(stories_path + fpath).parse_story())
                # for debugging, check log
                CreepyPastaGetter.story_writing_log(listing_fname=parsed_count, dest_fname=fpath, logname="parse_ok")
                parsed_count += 1
            except BaseException as e:
                CreepyPastaGetter.error_writing_log(e, error_count, fpath)
                error_count += 1
        return stories_dicts


"""
ADDITIONAL FUNCTIONS FOR ANALYSIS
"""
def get_creepypasta_authors(stories_df):
    from unidecode import unidecode
    return unidecode(", ".join(sorted(stories_df["author_str"].fillna("").unique())))

def format_stories_df(df):
    df["story_rating"] = df["story_rating"].apply(lambda x: float(x))
    df["reading_time_min"] = df["reading_time_min"].apply(lambda x: float(x))
    # TODO: swap to use entry-title for title instead?
    df["cleaned_title"] = df["title"].apply(lambda x: re.sub(r"\ *-\ *Creepypasta", "", x))

# TODO: integrate into csv export
def get_all_tags_list():
    categories_page = PageFetcherUtils.fetch_page(
        "https://www.creepypasta.com/archive/sorted-by-category/")
    soup = BeautifulSoup(resp.text)
    return [cat["value"] for cat in soup.findAll(
        "select", {"name" : "tx_category"})[0].select("option")][1:]

def get_df_with_expanded_story_cats_cols(df):
    cat_tag_links = get_all_tags_list()
    story_cats_df = df["story_cats"].apply(
        lambda story_cats: pd.Series(
            [cat in story_cats for cat in cat_tag_links], 
            index=cat_tag_links)).add_prefix("cat__")
    return pd.concat(
        [df, story_cats_df], axis=1)


if __name__ == "__main__":
    # Get/fetch and parse stories    
    stories_dict_list = get_stories_from_listings_dirpath("./list-pages/")
    # Load into dataframe for analysis
    stories_df = pd.DataFrame(stories_dict_list)
    # Write to disk
    stories_df.to_csv(f"./stories__{date.today()}.csv")
