Feature: Getting A Quote

  Scenario: Get a quote from default options
    Given I am a small business owner
    When I choose the default coverage options 
    And I choose to See Quote
    Then I get a quote of "245.025"
