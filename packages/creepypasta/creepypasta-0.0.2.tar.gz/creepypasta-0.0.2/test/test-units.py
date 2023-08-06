


class CreepyPastaGetterTestUnit:
    """
    Casual testing unit for `CreepyPastaGetter`.
    """
    @classmethod
    def test_fetch_pasta_pages(cls):
        # fetch per list-pages file, replace params
        CreepyPastaGetter.fetch_pasta_pages(
            list_page="test-list-page", 
            links_list=CreepyPastaSoupParserTestUnit.links_list)


class StoryListingsParserTestUnit:
    """
    Just a casual testing class.
    """
    @classmethod
    def test_parse_listings_get_story_links_per_page(cls, listing_fpath=None):
        example_listing_fpath = "./list-pages/2023-07-22__orderby=date&_page=29.html"
        listing_fpath = listing_fpath or example_listing_fpath
        story_links_dict = StoryListingsParser.parse_listings_get_story_links_per_page(listing_fpath)
        return story_links_dict
    
    @classmethod
    def test_get_all_story_links(cls, dir_path=None):
        example_dir_path = "./list-pages/"
        dir_path = dir_path or example_dir_path
        return StoryListingsParser.get_all_story_links(dir_path)
    
    @classmethod
    def test_write_json_of_story_links_dicts(cls, dir_path=None):
        example_dir_path = "./list-pages/"
        dir_path = dir_path or example_dir_path
        return StoryListingsParser.output_json(dir_path)


class CreepyPastaSoupParserTestUnit:
    test_files = [
        "./story-pages/published_stories_contamination.html",
        "./story-pages/published_stories_theo-twining.html",
        "./story-pages/published_stories_holder-of-eternity.html",
        "./story-pages/published_stories_the-kaleidoscope.html",
        "./story-pages/published_stories_the-town-of-blanche.html",
    ]
    links_list = [
        "https://www.creepypasta.com/contamination/",
        "https://www.creepypasta.com/holder-of-eternity/",
        "https://www.creepypasta.com/theo-twining/",
    ]
    
    @classmethod
    def test_parser_href(cls):
        parser = CreepyPastaSoupParser("https://www.creepypasta.com/gift-of-old/", is_fpath=False)
        return parser.parse_story()

    @classmethod
    def test_parser_fpath(cls):
        import random

        parser = CreepyPastaSoupParser(random.choice(cls.test_files), is_fpath=True)
        return parser.parse_story()
    
    @classmethod
    def test_parser_property(cls):
        import random

        parser = CreepyPastaSoupParser(random.choice(cls.test_files), is_fpath=True)
        return parser.published_date
