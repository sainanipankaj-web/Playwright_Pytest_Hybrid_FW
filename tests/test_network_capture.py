def test_network_capture(page):

    def capture_request(request):

        print(
            f"URL: {request.url}"
        )

        print(
            f"Method: {request.method}"
        )


    page.on(
        "request",
        capture_request
    )

    page.goto(
        "https://www.saucedemo.com"
    )