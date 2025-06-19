import asyncio
from playwright.async_api import async_playwright

FAUCET_URL = "https://testnet.pharosnetwork.xyz"
TESTNET_ADDRESS = "pharos1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your Pharos testnet address

async def claim_pharos_faucet():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Change to True to run headless
        page = await browser.new_page()

        await page.goto(FAUCET_URL)

        # Wait for the faucet input field - adjust selector based on actual page structure
        await page.wait_for_selector('input[type="text"], input[name="address"]')

        # Fill in your testnet wallet address
        await page.fill('input[type="text"], input[name="address"]', TESTNET_ADDRESS)

        # Click the faucet claim button - adjust selector as needed
        await page.click('button:has-text("Claim")')

        # Wait for confirmation or success message (adjust selector/text accordingly)
        try:
            await page.wait_for_selector('text=Success', timeout=10000)
            print("Faucet claim successful!")
        except:
            print("No success confirmation detected. Please check manually.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(claim_pharos_faucet())
