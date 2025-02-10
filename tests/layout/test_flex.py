"""Tests for flex layout."""

import pytest

from ..testing_utils import assert_no_logs, render_pages


@assert_no_logs
def test_flex_direction_row():
    page, = render_pages('''
      <article style="display: flex">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_y == div2.position_y == div3.position_y == article.position_y
    assert div1.position_x == article.position_x
    assert div1.position_x < div2.position_x < div3.position_x


@assert_no_logs
def test_flex_direction_row_max_width():
    page, = render_pages('''
      <article style="display: flex; max-width: 100px">
        <div></div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    assert article.width == 100


@assert_no_logs
def test_flex_direction_row_min_height():
    page, = render_pages('''
      <article style="display: flex; min-height: 100px">
        <div></div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    assert article.height == 100


@assert_no_logs
def test_flex_direction_row_rtl():
    page, = render_pages('''
      <article style="display: flex; direction: rtl">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_y == div2.position_y == div3.position_y == article.position_y
    assert div1.position_x + div1.width == article.position_x + article.width
    assert div1.position_x > div2.position_x > div3.position_x


@assert_no_logs
def test_flex_direction_row_reverse():
    page, = render_pages('''
      <article style="display: flex; flex-direction: row-reverse">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'C'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'A'
    assert div1.position_y == div2.position_y == div3.position_y == article.position_y
    assert div3.position_x + div3.width == article.position_x + article.width
    assert div1.position_x < div2.position_x < div3.position_x


@assert_no_logs
def test_flex_direction_row_reverse_rtl():
    page, = render_pages('''
      <article style="display: flex; flex-direction: row-reverse;
      direction: rtl">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'C'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'A'
    assert div1.position_y == div2.position_y == div3.position_y == article.position_y
    assert div3.position_x == article.position_x
    assert div1.position_x > div2.position_x > div3.position_x


@assert_no_logs
def test_flex_direction_column():
    page, = render_pages('''
      <article style="display: flex; flex-direction: column">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_x == div2.position_x == div3.position_x == article.position_x
    assert div1.position_y == article.position_y
    assert div1.position_y < div2.position_y < div3.position_y


@assert_no_logs
def test_flex_direction_column_min_width():
    page, = render_pages('''
      <article style="display: flex; flex-direction: column; min-height: 100px">
        <div></div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    assert article.height == 100


@assert_no_logs
def test_flex_direction_column_max_height():
    page, = render_pages('''
      <article style="display: flex; flex-flow: column wrap; max-height: 100px">
        <div style="height: 40px">A</div>
        <div style="height: 40px">B</div>
        <div style="height: 40px">C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    assert article.height == 100
    div1, div2, div3 = article.children
    assert div1.height == 40
    assert div1.position_x == 0
    assert div1.position_y == 0
    assert div2.height == 40
    assert div2.position_x == 0
    assert div2.position_y == 40
    assert div3.height == 40
    assert div3.position_x == div1.width
    assert div3.position_y == 0


@assert_no_logs
def test_flex_direction_column_rtl():
    page, = render_pages('''
      <article style="display: flex; flex-direction: column;
      direction: rtl">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_x == div2.position_x == div3.position_x == article.position_x
    assert div1.position_y == article.position_y
    assert div1.position_y < div2.position_y < div3.position_y


@assert_no_logs
def test_flex_direction_column_reverse():
    page, = render_pages('''
      <article style="display: flex; flex-direction: column-reverse">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'C'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'A'
    assert div1.position_x == div2.position_x == div3.position_x == article.position_x
    assert div3.position_y + div3.height == article.position_y + article.height
    assert div1.position_y < div2.position_y < div3.position_y


@assert_no_logs
def test_flex_direction_column_reverse_rtl():
    page, = render_pages('''
      <article style="display: flex; flex-direction: column-reverse;
      direction: rtl">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'C'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'A'
    assert div1.position_x == div2.position_x == div3.position_x == article.position_x
    assert div3.position_y + div3.height == article.position_y + article.height
    assert div1.position_y < div2.position_y < div3.position_y


@assert_no_logs
def test_flex_direction_column_box_sizing():
    page, = render_pages('''
      <style>
        article {
          box-sizing: border-box;
          display: flex;
          flex-direction: column;
          height: 10px;
          padding-top: 5px;
          width: 10px;
        }
      </style>
      <article></article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    assert article.width == 10
    assert article.height == 5
    assert article.padding_top == 5


@assert_no_logs
def test_flex_row_wrap():
    page, = render_pages('''
      <article style="display: flex; flex-flow: wrap; width: 50px">
        <div style="width: 20px">A</div>
        <div style="width: 20px">B</div>
        <div style="width: 20px">C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_y == div2.position_y == article.position_y
    assert div3.position_y == article.position_y + div2.height
    assert div1.position_x == div3.position_x == article.position_x
    assert div1.position_x < div2.position_x


@assert_no_logs
def test_flex_column_wrap():
    page, = render_pages('''
      <article style="display: flex; flex-flow: column wrap; height: 50px">
        <div style="height: 20px">A</div>
        <div style="height: 20px">B</div>
        <div style="height: 20px">C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_x == div2.position_x == article.position_x
    assert div3.position_x == article.position_x + div2.width
    assert div1.position_y == div3.position_y == article.position_y
    assert div1.position_y < div2.position_y


@assert_no_logs
def test_flex_row_wrap_reverse():
    page, = render_pages('''
      <article style="display: flex; flex-flow: wrap-reverse; width: 50px">
        <div style="width: 20px">A</div>
        <div style="width: 20px">B</div>
        <div style="width: 20px">C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'C'
    assert div2.children[0].children[0].text == 'A'
    assert div3.children[0].children[0].text == 'B'
    assert div1.position_y == article.position_y
    assert div2.position_y == div3.position_y == article.position_y + div1.height
    assert div1.position_x == div2.position_x == article.position_x
    assert div2.position_x < div3.position_x


@assert_no_logs
def test_flex_column_wrap_reverse():
    page, = render_pages('''
      <article style="display: flex; flex-flow: column wrap-reverse;
                      height: 50px">
        <div style="height: 20px">A</div>
        <div style="height: 20px">B</div>
        <div style="height: 20px">C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'C'
    assert div2.children[0].children[0].text == 'A'
    assert div3.children[0].children[0].text == 'B'
    assert div1.position_x == article.position_x
    assert div2.position_x == div3.position_x == article.position_x + div1.width
    assert div1.position_y == div2.position_y == article.position_y
    assert div2.position_y < div3.position_y


@assert_no_logs
def test_flex_direction_column_fixed_height_container():
    page, = render_pages('''
      <section style="height: 10px">
        <article style="display: flex; flex-direction: column">
          <div>A</div>
          <div>B</div>
          <div>C</div>
        </article>
      </section>
    ''')
    html, = page.children
    body, = html.children
    section, = body.children
    article, = section.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_x == div2.position_x == div3.position_x == article.position_x
    assert div1.position_y == article.position_y
    assert div1.position_y < div2.position_y < div3.position_y
    assert section.height == 10
    assert article.height > 10


@assert_no_logs
def test_flex_direction_column_fixed_height():
    page, = render_pages('''
      <article style="display: flex; flex-direction: column; height: 10px">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_x == div2.position_x == div3.position_x == article.position_x
    assert div1.position_y == article.position_y
    assert div1.position_y < div2.position_y < div3.position_y
    assert article.height == 10
    assert div3.position_y > 10


@assert_no_logs
def test_flex_direction_column_fixed_height_wrap():
    page, = render_pages('''
      <article style="display: flex; flex-direction: column; height: 10px;
                      flex-wrap: wrap">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_x < div2.position_x < div3.position_x
    assert div1.position_y == article.position_y
    assert div1.position_y == div2.position_y == div3.position_y == article.position_y
    assert article.height == 10


@assert_no_logs
def test_flex_direction_column_break():
    # Regression test for issue #2066.
    page1, page2 = render_pages('''
      <style>
        @page { size: 4px 5px }
      </style>
      <article style="display: flex; flex-direction: column; font: 2px weasyprint">
        <div>A<br>B<br>C</div>
      </article>
    ''')
    html, = page1.children
    body, = html.children
    article, = body.children
    div, = article.children
    assert div.children[0].children[0].text == 'A'
    assert div.children[1].children[0].text == 'B'
    assert div.height == 5
    html, = page2.children
    body, = html.children
    article, = body.children
    div, = article.children
    assert div.children[0].children[0].text == 'C'
    assert div.height == 2


@assert_no_logs
def test_flex_direction_column_break_border():
    page1, page2 = render_pages('''
      <style>
        @page { size: 8px 7px }
        article, div { border: 1px solid black }
      </style>
      <article style="display: flex; flex-direction: column; font: 2px weasyprint">
        <div>A B C</div>
      </article>
    ''')
    html, = page1.children
    body, = html.children
    article, = body.children
    assert article.border_height() == 7
    assert article.border_top_width == 1
    assert article.border_bottom_width == 0
    div, = article.children
    assert div.children[0].children[0].text == 'A'
    assert div.children[1].children[0].text == 'B'
    assert div.border_height() == 6
    assert div.border_top_width == 1
    assert div.border_bottom_width == 0
    html, = page2.children
    body, = html.children
    article, = body.children
    assert article.border_height() == 4
    assert article.border_top_width == 0
    assert article.border_bottom_width == 1
    div, = article.children
    assert div.children[0].children[0].text == 'C'
    assert div.border_height() == 3
    assert div.border_top_width == 0
    assert div.border_bottom_width == 1


@assert_no_logs
def test_flex_item_min_width():
    page, = render_pages('''
      <article style="display: flex">
        <div style="min-width: 30px">A</div>
        <div style="min-width: 50px">B</div>
        <div style="min-width: 5px">C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_x == 0
    assert div1.width == 30
    assert div2.position_x == 30
    assert div2.width == 50
    assert div3.position_x == 80
    assert div3.width > 5
    assert div1.position_y == div2.position_y == div3.position_y == article.position_y


@assert_no_logs
def test_flex_item_min_height():
    page, = render_pages('''
      <article style="display: flex">
        <div style="min-height: 30px">A</div>
        <div style="min-height: 50px">B</div>
        <div style="min-height: 5px">C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.height == div2.height == div3.height == article.height == 50


@assert_no_logs
def test_flex_auto_margin():
    # Regression test for issue #800.
    page, = render_pages('<div id="div1" style="display: flex; margin: auto">')
    page, = render_pages(
        '<div id="div2" style="display: flex; flex-direction: column; margin: auto">')


@assert_no_logs
def test_flex_no_baseline():
    # Regression test for issue #765.
    page, = render_pages('''
      <div class="references" style="display: flex; align-items: baseline;">
        <div></div>
      </div>''')


@assert_no_logs
@pytest.mark.parametrize('align, height, y1, y2', (
    ('flex-start', 50, 0, 10),
    ('flex-end', 50, 30, 40),
    ('space-around', 60, 10, 40),
    ('space-between', 50, 0, 40),
    ('space-evenly', 50, 10, 30),
))
def test_flex_align_content(align, height, y1, y2):
    # Regression test for issue #811.
    page, = render_pages('''
      <style>
        article {
          align-content: %s;
          display: flex;
          flex-wrap: wrap;
          font-family: weasyprint;
          font-size: 10px;
          height: %dpx;
          line-height: 1;
        }
        section {
          width: 100%%;
        }
      </style>
      <article>
        <section><span>Lorem</span></section>
        <section><span>Lorem</span></section>
      </article>
    ''' % (align, height))
    html, = page.children
    body, = html.children
    article, = body.children
    section1, section2 = article.children
    line1, = section1.children
    line2, = section2.children
    span1, = line1.children
    span2, = line2.children
    assert section1.position_x == span1.position_x == 0
    assert section1.position_y == span1.position_y == y1
    assert section2.position_x == span2.position_x == 0
    assert section2.position_y == span2.position_y == y2


@assert_no_logs
def test_flex_item_percentage():
    # Regression test for issue #885.
    page, = render_pages('''
      <div style="display: flex; font-size: 15px; line-height: 1">
        <div style="height: 100%">a</div>
      </div>''')
    html, = page.children
    body, = html.children
    flex, = body.children
    flex_item, = flex.children
    assert flex_item.height == 15


@assert_no_logs
def test_flex_undefined_percentage_height_multiple_lines():
    # Regression test for issue #1204.
    page, = render_pages('''
      <div style="display: flex; flex-wrap: wrap; height: 100%">
        <div style="width: 100%">a</div>
        <div style="width: 100%">b</div>
      </div>''')


@assert_no_logs
def test_flex_absolute():
    # Regression test for issue #1536.
    page, = render_pages('''
      <div style="display: flex; position: absolute">
        <div>a</div>
      </div>''')


@assert_no_logs
def test_flex_percent_height():
    page, = render_pages('''
      <style>
        .a { height: 10px; width: 10px; }
        .b { height: 10%; width: 100%; display: flex; flex-direction: column; }
      </style>
      <div class="a"">
        <div class="b"></div>
      </div>''')
    html, = page.children
    body, = html.children
    a, = body.children
    b, = a.children
    assert a.height == 10
    assert b.height == 1


@assert_no_logs
def test_flex_percent_height_auto():
    # Regression test for issue #2146.
    page, = render_pages('''
      <style>
        .a { width: 10px; }
        .b { height: 10%; width: 100%; display: flex; flex-direction: column; }
      </style>
      <div class="a"">
        <div class="b"></div>
      </div>''')


@assert_no_logs
def test_flex_break_inside_avoid():
    # Regression test for issue #2183.
    page1, page2= render_pages('''
      <style>
        @page { size: 6px 4px }
        html { font-family: weasyprint; font-size: 2px }
      </style>
      <article style="display: flex; flex-wrap: wrap">
        <div>ABC</div>
        <div style="break-inside: avoid">abc def</div>
      </article>''')
    html, = page1.children
    body, = html.children
    article, = body.children
    div, = article.children
    html, = page2.children
    body, = html.children
    article, = body.children
    div, = article.children


@assert_no_logs
def test_flex_absolute_content():
    # Regression test for issue #996.
    page, = render_pages('''
      <section style="display: flex; position: relative">
         <h1 style="position: absolute; top: 0; right: 0">TEST</h1>
         <p>Hello world!</p>
      </section>''')
    html, = page.children
    body, = html.children
    section, = body.children
    h1, p = section.children
    assert h1.position_x != 0
    assert h1.position_y == 0
    assert p.position_x == 0
    assert p.position_y == 0


@assert_no_logs
def test_flex_column_height():
    # Regression test for issue #2222.
    page, = render_pages("""
      <section style="display: flex; width: 10em">
        <article style="display: flex; flex-direction: column">
          <div>
            Lorem ipsum dolor sit amet
          </div>
        </article>
        <article style="display: flex; flex-direction: column">
          <div>
            Lorem ipsum dolor sit amet
          </div>
        </article>
      </section>
    """)
    html, = page.children
    body, = html.children
    section, = body.children
    article1, article2 = section.children
    assert article1.height == section.height
    assert article2.height == section.height


@assert_no_logs
def test_flex_column_height_margin():
    # Regression test for issue #2222.
    page, = render_pages("""
      <section style="display: flex; flex-direction: column; width: 10em">
        <article style="margin: 5px">
          Lorem ipsum dolor sit amet
        </article>
        <article style="margin: 10px">
          Lorem ipsum dolor sit amet
        </article>
      </section>
    """)
    html, = page.children
    body, = html.children
    section, = body.children
    article1, article2 = section.children
    assert section.height == article1.margin_height() + article2.margin_height()


@assert_no_logs
def test_flex_column_width():
    # Regression test for issue #1171.
    page, = render_pages("""
      <style>
        #paper {
          display: flex;
          flex-direction: column;
          height: 400px;
          width: 500px;
        }
        #content {
          display: flex;
          flex: auto;
          flex-direction: column;
          justify-content: space-between;
          width: 100%;
        }
        #header {
          height: 50px;
          width: 100%;
        }
      </style>
      <div id="paper">
        <div id="header">Header</div>
        <div id="content">
          <div>Middle</div>
          <div>Bottom</div>
        </div>
      </div>
    """)
    html, = page.children
    body, = html.children
    paper, = body.children
    header, content = paper.children
    top, bottom = content.children
    assert header.width == paper.width
    assert content.width == paper.width
    assert top.width == paper.width
    assert bottom.position_y > top.position_y + top.height


@assert_no_logs
def test_flex_auto_margin2():
    # Regression test for issue #2054.
    page, = render_pages('''
      <style>
        #outer {
          background: red;
        }
        #inner {
          margin: auto;
          display: flex;
          width: 160px;
          height: 160px;
          background: black;
        }
      </style>
      <div id="outer">
        <div id="inner"></div>
      </div>
    ''')
    html, = page.children
    body, = html.children
    outer, = body.children
    inner, = outer.children
    assert inner.margin_left != 0


@assert_no_logs
def test_flex_overflow():
    # Regression test for issue #2292.
    page, = render_pages('''
      <style>
        article {
          display: flex;
        }
        section {
          overflow: hidden;
          width: 5px;
        }
      </style>
      <article>
        <section>A</section>
        <section>B</section>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    section_1 = article.children[0]
    section_2 = article.children[1]
    assert section_1.position_x == 0
    assert section_2.position_x == 5


@assert_no_logs
def test_flex_column_overflow():
    # Regression test for issue #2304.
    render_pages('''
      <style>
        @page {size: 20px}
      </style>
      <div style="display: flex; flex-direction: column">
        <div></div>
        <div><div style="height: 40px"></div></div>
        <div><div style="height: 5px"></div></div>
      </div>
    ''')


@assert_no_logs
def test_inline_flex():
    render_pages('''
      <style>
        @page {size: 20px}
      </style>
      <div style="display: inline-flex; flex-direction: column">
        <div>test</div>
      </div>
    ''')


@assert_no_logs
def test_inline_flex_empty_child():
    render_pages('''
      <style>
        @page {size: 20px}
      </style>
      <div style="display: inline-flex; flex-direction: column">
        <div></div>
      </div>
    ''')


@assert_no_logs
def test_inline_flex_absolute_baseline():
    render_pages('''
      <style>
        @page {size: 20px}
      </style>
      <div style="display: inline-flex; flex-direction: column">
        <div style="position: absolute">abs</div>
      </div>
    ''')


@assert_no_logs
def test_flex_item_overflow():
    # Regression test for issue #2359.
    page, = render_pages('''
      <div style="display: flex; font: 2px weasyprint; width: 12px">
        <div>ab</div>
        <div>c d e</div>
        <div>f</div>
      </div>''')
    html, = page.children
    body, = html.children
    flex, = body.children
    div1, div2, div3 = flex.children
    assert div1.width == 4
    assert div2.width == 6
    assert div3.width == 2
    line1, line2 = div2.children
    text1, = line1.children
    text2, = line2.children
    assert text1.text == 'c d'
    assert text2.text == 'e'


@assert_no_logs
def test_flex_direction_row_inline_block():
    # Regression test for issue #1652.
    page, = render_pages('''
      <article style="display: flex; font: 2px weasyprint; width: 14px">
        <div style="display: inline-block">A B C D E F</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div, = article.children
    assert div.width == 14
    assert div.children[0].children[0].text == 'A B C D'
    assert div.children[1].children[0].text == 'E F'


@assert_no_logs
def test_flex_float():
    page, = render_pages('''
      <article style="display: flex">
        <div style="float: left">A</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div, = article.children
    assert div.children[0].children[0].text == 'A'


@assert_no_logs
def test_flex_float_in_flex_item():
    # Regression test for issue #1356.
    page, = render_pages('''
      <article style="display: flex; font: 2px weasyprint">
        <div style="width: 10px"><span style="float: right">abc</span></div>
        <div style="width: 10px"><span style="float: right">abc</span></div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2 = article.children
    span1, = div1.children
    assert span1.position_y == 0
    assert span1.position_x + span1.width == 10
    span2, = div2.children
    assert span2.position_y == 0
    assert span2.position_x + span2.width == 20


@assert_no_logs
def test_flex_direction_row_defined_main():
    page, = render_pages('''
      <article style="display: flex">
        <div style="width: 10px; padding: 1px"></div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div, = article.children
    assert div.width == 10
    assert div.margin_width() == 12


@assert_no_logs
def test_flex_direction_row_defined_main_border_box():
    page, = render_pages('''
      <article style="display: flex">
        <div style="box-sizing: border-box; width: 10px; padding: 1px"></div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div, = article.children
    assert div.width == 8
    assert div.margin_width() == 10


@assert_no_logs
def test_flex_direction_column_defined_main():
    page, = render_pages('''
      <article style="display: flex; flex-direction: column">
        <div style="height: 10px; padding: 1px"></div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div, = article.children
    assert div.height == 10
    assert div.margin_height() == 12


@assert_no_logs
def test_flex_direction_column_defined_main_border_box():
    page, = render_pages('''
      <article style="display: flex; flex-direction: column">
        <div style="box-sizing: border-box; height: 10px; padding: 1px"></div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div, = article.children
    assert div.height == 8
    assert div.margin_height() == 10


@assert_no_logs
def test_flex_item_negative_margin():
    page, = render_pages('''
      <article style="display: flex">
        <div style="margin-left: -20px; height: 10px; width: 10px"></div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div, = article.children
    assert div.height == 10
    assert div.width == 10


@assert_no_logs
def test_flex_item_auto_margin():
    page, = render_pages('''
      <article style="display: flex">
        <div style="margin-left: auto; height: 10px; width: 10px"></div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div, = article.children
    assert div.height == 10
    assert div.width == 10


@assert_no_logs
def test_flex_item_auto_margin_flex_basis():
    page, = render_pages('''
      <article style="display: flex">
        <div style="margin-left: auto; height: 10px; flex-basis: 10px"></div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div, = article.children
    assert div.height == 10
    assert div.width == 10


@assert_no_logs
@pytest.mark.parametrize('align, x1, x2, x3', (
    ('start', 0, 2, 4),
    ('flex-start', 0, 2, 4),
    ('left', 0, 2, 4),
    ('end', 6, 8, 10),
    ('flex-end', 6, 8, 10),
    ('right', 6, 8, 10),
    ('center', 3, 5, 7),
    ('space-between', 0, 5, 10),
    ('space-around', 1, 5, 9),
    ('space-evenly', 1.5, 5, 8.5),
))
def test_flex_direction_row_justify(align, x1, x2, x3):
    page, = render_pages(f'''
      <article style="width: 12px; font: 2px weasyprint;
                      display: flex; justify-content: {align}">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_y == div2.position_y == div3.position_y == article.position_y
    assert article.position_x == 0
    assert div1.position_x == x1
    assert div2.position_x == x2
    assert div3.position_x == x3


@assert_no_logs
@pytest.mark.parametrize('align, y1, y2, y3', (
    ('start', 0, 2, 4),
    ('flex-start', 0, 2, 4),
    ('left', 0, 2, 4),
    ('end', 6, 8, 10),
    ('flex-end', 6, 8, 10),
    ('right', 6, 8, 10),
    ('center', 3, 5, 7),
    ('space-between', 0, 5, 10),
    ('space-around', 1, 5, 9),
    ('space-evenly', 1.5, 5, 8.5),
))
def test_flex_direction_column_justify(align, y1, y2, y3):
    page, = render_pages(f'''
      <article style="height: 12px; font: 2px weasyprint;
                      display: flex; flex-direction: column; justify-content: {align}">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_x == div2.position_x == div3.position_x == article.position_x
    assert article.position_y == 0
    assert div1.position_y == y1
    assert div2.position_y == y2
    assert div3.position_y == y3


@assert_no_logs
@pytest.mark.parametrize('align, x1, x2, x3', (
    ('start', 0, 4, 8),
    ('flex-start', 0, 4, 8),
    ('left', 0, 4, 8),
    ('end', 6, 10, 14),
    ('flex-end', 6, 10, 14),
    ('right', 6, 10, 14),
    ('center', 3, 7, 11),
    ('space-between', 0, 7, 14),
    ('space-around', 1, 7, 13),
    ('space-evenly', 1.5, 7, 12.5),
))
def test_flex_direction_row_justify_gap(align, x1, x2, x3):
    page, = render_pages(f'''
      <article style="width: 16px; font: 2px weasyprint; gap: 2px;
                      display: flex; justify-content: {align}">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_y == div2.position_y == div3.position_y == article.position_y
    assert article.position_x == 0
    assert div1.position_x == x1
    assert div2.position_x == x2
    assert div3.position_x == x3


@assert_no_logs
@pytest.mark.parametrize('align, y1, y2, y3', (
    ('start', 0, 4, 8),
    ('flex-start', 0, 4, 8),
    ('left', 0, 4, 8),
    ('end', 6, 10, 14),
    ('flex-end', 6, 10, 14),
    ('right', 6, 10, 14),
    ('center', 3, 7, 11),
    ('space-between', 0, 7, 14),
    ('space-around', 1, 7, 13),
    ('space-evenly', 1.5, 7, 12.5),
))
def test_flex_direction_column_justify_gap(align, y1, y2, y3):
    page, = render_pages(f'''
      <article style="height: 16px; font: 2px weasyprint; gap: 2px;
                      display: flex; flex-direction: column; justify-content: {align}">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_x == div2.position_x == div3.position_x == article.position_x
    assert article.position_y == 0
    assert div1.position_y == y1
    assert div2.position_y == y2
    assert div3.position_y == y3


@assert_no_logs
@pytest.mark.parametrize('align, x1, x2, x3', (
    ('start', 0, 4, 0),
    ('flex-start', 0, 4, 0),
    ('left', 0, 4, 0),
    ('end', 3, 7, 7),
    ('flex-end', 3, 7, 7),
    ('right', 3, 7, 7),
    ('center', 1.5, 5.5, 3.5),
    ('space-between', 0, 7, 0),
    ('space-around', 0.75, 6.25, 3.5),
    ('space-evenly', 1, 6, 3.5),
))
def test_flex_direction_row_justify_gap_wrap(align, x1, x2, x3):
    page, = render_pages(f'''
      <article style="width: 9px; font: 2px weasyprint; gap: 1px 2px;
                      display: flex; flex-wrap: wrap; justify-content: {align}">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_y == div2.position_y == article.position_y == 0
    assert div3.position_y == 3
    assert article.position_x == 0
    assert div1.position_x == x1
    assert div2.position_x == x2
    assert div3.position_x == x3


@assert_no_logs
@pytest.mark.parametrize('align, y1, y2, y3', (
    ('start', 0, 4, 0),
    ('flex-start', 0, 4, 0),
    ('left', 0, 4, 0),
    ('end', 3, 7, 7),
    ('flex-end', 3, 7, 7),
    ('right', 3, 7, 7),
    ('center', 1.5, 5.5, 3.5),
    ('space-between', 0, 7, 0),
    ('space-around', 0.75, 6.25, 3.5),
    ('space-evenly', 1, 6, 3.5),
))
def test_flex_direction_column_justify_gap_wrap(align, y1, y2, y3):
    page, = render_pages(f'''
      <article style="height: 9px; width: 9px; font: 2px weasyprint; gap: 2px 1px;
                      display: flex; flex-wrap: wrap; flex-direction: column;
                      justify-content: {align}">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_x == div2.position_x == article.position_x == 0
    assert div3.position_x == 5
    assert article.position_y == 0
    assert div1.position_y == y1
    assert div2.position_y == y2
    assert div3.position_y == y3


@assert_no_logs
def test_flex_direction_row_stretch_no_grow():
    page, = render_pages('''
      <article style="font: 2px weasyprint; width: 10px;
                      display: flex; justify-content: stretch">
        <div>A</div>
        <div>B</div>
        <div>C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_y == div2.position_y == div3.position_y == article.position_y
    assert div1.width == div2.width == div3.width == 2
    assert div1.position_x == article.position_x == 0
    assert div2.position_x == 2
    assert div3.position_x == 4


@assert_no_logs
def test_flex_direction_row_stretch_grow():
    page, = render_pages('''
      <article style="font: 2px weasyprint; width: 10px;
                      display: flex; justify-content: stretch">
        <div>A</div>
        <div style="flex-grow: 3">B</div>
        <div style="flex-grow: 1">C</div>
      </article>
    ''')
    html, = page.children
    body, = html.children
    article, = body.children
    div1, div2, div3 = article.children
    assert div1.children[0].children[0].text == 'A'
    assert div2.children[0].children[0].text == 'B'
    assert div3.children[0].children[0].text == 'C'
    assert div1.position_y == div2.position_y == div3.position_y == article.position_y
    assert div1.width == 2
    assert div2.width == 5
    assert div3.width == 3
    assert div1.position_x == article.position_x == 0
    assert div2.position_x == 2
    assert div3.position_x == 7
