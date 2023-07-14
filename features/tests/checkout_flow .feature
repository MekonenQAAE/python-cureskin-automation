# Created by Owner at 7/13/2023
Feature: Checkout flow

  Scenario: User can add a product to a cart
    Given Open product details page https://shop.cureskin.com/collections/face-wash/products/gentle-cleanse-face-foam
    When Click to add product to cart
    Then Verify "added to your cart" confirmation is shown
    When Click "View my cart"
    Then Verify user is taken to the cart page