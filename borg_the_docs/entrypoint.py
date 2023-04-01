#!/usr/bin/env python3
import argparse
import os

from ntd2d_action.action import NISTtheDocs2Death

def main():
    action = os.environ['INPUT_ACTION']

    if action == 'update_pages':
        ntd2d = NISTtheDocs2Death(docs_dir=os.environ['INPUT_DOCS-FOLDER'],
                                  default_branch=os.environ['INPUT_DEFAULT-BRANCH'],
                                  pages_branch=os.environ['INPUT_PAGES-BRANCH'],
                                  pages_url=os.environ['INPUT_PAGES-URL'])
        ntd2d.update_pages()
    elif action == 'borg_the_docs':
        print("Borging the docs")

if __name__ == "__main__":
    main()
