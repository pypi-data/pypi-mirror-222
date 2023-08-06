import gradio as gr
import os
from html_content_extractor import extract_content
from playwright.sync_api import sync_playwright


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.join(CURRENT_DIR, "html_examples")


def scrape_and_extract(url, format):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state()
        html = page.content()

    return extract_content(html, format=format)


def scrape_as_markdown(url):
    return scrape_and_extract(url, format="markdown")


def scrape_as_plaintext(url):
    return scrape_and_extract(url, format="plaintext")


with gr.Blocks() as demo:
    url = gr.Textbox(placeholder="Enter a URL", show_label=False)
    with gr.Box():
        md = gr.Markdown("Output will appear here")
    pt = gr.Textbox(
        placeholder="Output will appear here",
        label="Most relevant text from page.",
    )

    ptbtn = gr.Button("Extract as plaintext")
    ptbtn.click(fn=scrape_as_plaintext, inputs=url, outputs=pt)

    mdbtn = gr.Button("Extract as markdown")
    mdbtn.click(fn=scrape_as_markdown, inputs=url, outputs=md)

demo.launch(inbrowser=True)
