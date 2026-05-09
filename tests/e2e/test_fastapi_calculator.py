# tests/e2e/test_fastapi_calculator.py

from uuid import uuid4
import pytest


BASE_URL = "http://localhost:8000"


def get_base_url(fastapi_server):
    return fastapi_server.rstrip("/") if fastapi_server else BASE_URL


def register_and_login(page, base_url):
    unique = uuid4().hex[:8]
    username = f"e2euser_{unique}"
    email = f"e2euser_{unique}@example.com"
    password = "GoodPass123!"

    page.goto(f"{base_url}/register")

    page.fill("#registerUsername", username)
    page.fill("#registerEmail", email)
    page.fill("#registerFirstName", "E2E")
    page.fill("#registerLastName", "User")
    page.fill("#registerPassword", password)
    page.fill("#registerConfirmPassword", password)
    page.click('button:has-text("Create Account")')

    page.wait_for_url(f"{base_url}/login", timeout=5000)

    page.fill("#loginUsername", username)
    page.fill("#loginPassword", password)
    page.click('button:has-text("Sign In")')

    page.wait_for_url(f"{base_url}/dashboard", timeout=5000)


def create_calculation(page, operation, a, b, expected_result):
    page.fill("#calcA", str(a))
    page.fill("#calcB", str(b))
    page.click(f'button[data-value="{operation}"]')
    page.click('button:has-text("Calculate")')

    page.locator("#dashboardSuccess").wait_for(state="visible")
    assert f"Result: {expected_result}" in page.inner_text("#dashboardSuccess")

    row = page.locator("#calculationsTable tr").filter(has_text=operation).first
    row.wait_for(state="visible")
    return row


@pytest.mark.e2e
def test_calculation_bread_flow(page, fastapi_server):
    base_url = get_base_url(fastapi_server)
    register_and_login(page, base_url)

    create_calculation(page, "addition", 10, 5, 15)

    page.click('a:has-text("View")')
    page.wait_for_url("**/dashboard/view/**")
    page.locator("#calculationCard").wait_for(state="visible")
    view_url = page.url
    assert "Calculation Details" in page.inner_text("body")
    assert "15" in page.inner_text("body")

    page.click('a:has-text("Edit")')
    page.wait_for_url("**/dashboard/edit/**")
    page.fill("#a", "20")
    page.fill("#b", "4")
    page.select_option("#type", "division")

    with page.expect_response(
        lambda response: "/calculations/" in response.url
        and response.request.method == "PUT",
        timeout=5000,
    ) as update_response_info:
        page.click('button:has-text("Save Changes")')

    assert update_response_info.value.ok

    page.goto(view_url)

    page.locator("#calculationCard").wait_for(state="visible")

    assert page.inner_text("#calcType") == "Division"
    assert page.inner_text("#calcA") == "20"
    assert page.inner_text("#calcB") == "4"
    assert page.inner_text("#calcResult") == "5"

    page.on("dialog", lambda dialog: dialog.accept())
    page.click('button:has-text("Delete")')
    page.wait_for_url(f"{base_url}/dashboard", timeout=5000)


@pytest.mark.e2e
def test_invalid_calculation_input(page, fastapi_server):
    base_url = get_base_url(fastapi_server)
    register_and_login(page, base_url)

    page.fill("#calcA", "10")
    page.fill("#calcB", "0")
    page.click('button[data-value="division"]')
    page.click('button:has-text("Calculate")')

    page.locator("#dashboardError").wait_for(state="visible")
    assert page.inner_text("#dashboardError") == "Division by zero is not allowed."


@pytest.mark.e2e
def test_power_calculation_flow(page, fastapi_server):
    base_url = get_base_url(fastapi_server)
    register_and_login(page, base_url)

    row = create_calculation(page, "power", 2, 3, 8)
    row.locator('a:has-text("View")').click()

    page.wait_for_url("**/dashboard/view/**")
    page.locator("#calculationCard").wait_for(state="visible")

    assert page.inner_text("#calcType") == "Power"
    assert page.inner_text("#calcA") == "2"
    assert page.inner_text("#calcB") == "3"
    assert page.inner_text("#visualOperator") == "^"
    assert page.inner_text("#calcResult") == "8"


@pytest.mark.e2e
def test_modulus_calculation_flow(page, fastapi_server):
    base_url = get_base_url(fastapi_server)
    register_and_login(page, base_url)

    row = create_calculation(page, "modulus", 10, 3, 1)
    row.locator('a:has-text("View")').click()

    page.wait_for_url("**/dashboard/view/**")
    page.locator("#calculationCard").wait_for(state="visible")

    assert page.inner_text("#calcType") == "Modulus"
    assert page.inner_text("#calcA") == "10"
    assert page.inner_text("#calcB") == "3"
    assert page.inner_text("#visualOperator") == "%"
    assert page.inner_text("#calcResult") == "1"


@pytest.mark.e2e
def test_modulus_by_zero_input(page, fastapi_server):
    base_url = get_base_url(fastapi_server)
    register_and_login(page, base_url)

    page.fill("#calcA", "10")
    page.fill("#calcB", "0")
    page.click('button[data-value="modulus"]')
    page.click('button:has-text("Calculate")')

    page.locator("#dashboardError").wait_for(state="visible")
    assert page.inner_text("#dashboardError") == "Modulus by zero is not allowed."


@pytest.mark.e2e
def test_unauthorized_dashboard_redirect(page, fastapi_server):
    base_url = get_base_url(fastapi_server)

    page.goto(f"{base_url}/dashboard")
    page.wait_for_url(f"{base_url}/login", timeout=5000)
    assert "Sign in" in page.inner_text("body")
