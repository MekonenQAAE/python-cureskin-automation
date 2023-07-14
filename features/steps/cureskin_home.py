from behave import given, when, then


@given('Open product details page {url}')
def open_url(context, url):
    context.app.home_page.open_product_details(url)