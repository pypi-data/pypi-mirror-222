import inspect
import pprint

import mknodes

from mknodes.utils import classhelpers


INTRO_TEXT = """Lets show some info about the tree we built.
The tree starts from the root nav down to the Markup elements.
"""

SECTION_CODE = "Code for this section"
PAGE_CODE = "Code for this page"


def create_internals_section(root_nav: mknodes.MkNav):
    internals_nav = root_nav.add_nav("Internals")

    overview = internals_nav.add_index_page(hide_toc=True, icon="material/magnify")
    overview += mknodes.MkCode.for_object(create_internals_section, header=SECTION_CODE)
    overview += mknodes.MkDetailsBlock(INTRO_TEXT)

    # the "Tree" section in the left sidebar shows what we have done up to now.
    create_tree_page(internals_nav)
    # Each tree item can carry virtual files.
    # Lets dispay all files which are currently attached to the tree:
    create_file_tree_page(internals_nav)
    create_code_page(internals_nav)


def create_tree_page(nav: mknodes.MkNav):
    # we create a new page and add a formatted represenation of our Tree.

    page = nav.add_page("Tree", hide_toc=True, icon="material/graph")
    page += mknodes.MkCode.for_object(create_tree_page, header=PAGE_CODE)
    page.add_header("This is the tree we built up to now.", level=3)
    lines = [f"{level * '    '} {node!r}" for level, node in nav.root.iter_nodes()]
    page += mknodes.MkCode("\n".join(lines))


def create_file_tree_page(nav: mknodes.MkNav):
    page = nav.add_page("Files", hide_toc=True, icon="material/file-tree-outline")
    page += mknodes.MkCode.for_object(create_file_tree_page, header=PAGE_CODE)
    page.add_header("These are the 'virtual' files attached to the tree:", level=3)
    # we want to see all files, so we have to go through the root nav:
    virtual_files = nav.root.all_virtual_files()
    file_txt = pprint.pformat(list(virtual_files.keys()))
    page += mknodes.MkCode(file_txt)


def create_code_page(nav: mknodes.MkNav):
    # To show what was needed to create this page, we`ll create a section.
    from mknodes import manual

    code_nav = nav.add_nav("Complete code")
    index = code_nav.add_index_page(hide_toc=True, icon="octicons/code-24")
    index += mknodes.MkCode.for_object(create_code_page, header=SECTION_CODE)
    for _module_name, module in inspect.getmembers(manual, inspect.ismodule):
        filename = module.__name__.split(".")[-1] + ".py"
        page = code_nav.add_page(filename, hide_toc=True)
        page += mknodes.MkCode.for_object(module, title=filename)
    example_page = code_nav.add_page("create_example_page methods")
    for kls in classhelpers.iter_subclasses(mknodes.MkNode):
        # iter_subclasses just calls __subclasses__ recursively.
        if "create_example_page" not in kls.__dict__:
            continue
        header = kls.__name__
        example_page += mknodes.MkCode.for_object(kls.create_example_page, header=header)
