import mknodes


INTRO_TEXT = """MkNodes also contains some higher-order nodes to quickly put together
a Development section.
"""

SECTION_CODE = "Code for this section"
PAGE_CODE = "Code for this page"


def create_development_section(root_nav: mknodes.MkNav):
    dev_nav = root_nav.add_nav("Development")
    overview = dev_nav.add_index_page(hide_toc=True, icon="fontawesome/solid/layer-group")
    overview += mknodes.MkCode.for_object(create_development_section, header=SECTION_CODE)
    overview += mknodes.MkAdmonitionBlock(INTRO_TEXT)
    create_changelog_page(dev_nav)
    create_coc_page(dev_nav)
    create_contribute_page(dev_nav)


def create_changelog_page(nav: mknodes.MkNav):
    page = nav.add_page("Changelog", icon="material/format-list-group")
    page += mknodes.MkCode.for_object(create_changelog_page, header=PAGE_CODE)
    page += mknodes.MkChangelog()  # based on "git-changelog" package


def create_coc_page(nav: mknodes.MkNav):
    page = nav.add_page("Code of conduct", icon="octicons/code-of-conduct-24")
    page += mknodes.MkCode.for_object(create_coc_page, header=PAGE_CODE)
    page += mknodes.MkCodeOfConduct(contact_email="philipptemminghoff@gmail.com")


def create_contribute_page(nav: mknodes.MkNav):
    page = nav.add_page("Contributing", icon="material/help")
    page += mknodes.MkCode.for_object(create_contribute_page, header=PAGE_CODE)
    page += mknodes.MkCommitMessageConvention()
    page += mknodes.MkPullRequestGuidelines()
