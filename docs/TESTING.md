# Quality Shares - Automated Testing

The Django project has three apps (about, blog and portfolio), each of which has a `test_views.py` file containing unit tests.

## About App Tests

|Test Class|Test Method|Status|
|---|---|---|
|TestAboutView|test_about_page|Pass|

## Blog App Tests

|Test Class|Test Method|Status|
|---|---|---|
|TestBlogViews|test_post_list_view|Pass|
|TestBlogViews|test_post_detail_view|Pass|
|TestBlogViews|test_category_list_view|Pass|
|TestBlogViews|test_new_comment_submission|Pass|

Tests for editing and deleting comments would have been ideal, but these were not a required part of the project and were deferred due to time constraints.

## Portfolio App Tests

|Test Class|Test Method|Status|
|---|---|---|
|TestPortfolioView|test_portfolio_page|Pass|

