// Replace with your actual API access token
const API_TOKEN = "c5zfA3pbErdt9g_OFZ0sL4iDPeDKvJcY1m6UIX7OjtUe7pWGEH3hQV3twZsXjTQ5O-4";

// Assuming you have unique IDs for each select element
const countrySelect = document.getElementById("country");
const stateSelect = document.getElementById("state");
const citySelect = document.getElementById("city");

// Function to fetch and populate countries
async function fetchCountries() {
  try {
    const response = await fetch("https://www.universal-tutorial.com/api/countries/", {
      headers: {
        "Accept": "application/json",
        "api-token": API_TOKEN,
        "user-email": "nyarashbayev97@gmail.com"
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const countries = await response.json();
    populateDropdown(countrySelect, countries, 'country_name');
  } catch (error) {
    console.error('Error fetching countries:', error);
    // Handle error (e.g., display an error message to the user)
  }
}

// Function to fetch and populate states based on selected country
async function fetchStates() {
  const selectedCountry = countrySelect.value;

  try {
    const response = await fetch(`https://www.universal-tutorial.com/api/states/${selectedCountry}`, {
      headers: {
        "Accept": "application/json",
        "api-token": API_TOKEN,
        "user-email": "nyarashbayev97@gmail.com"
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const states = await response.json();
    populateDropdown(stateSelect, states, 'state_name');
    // Clear city selection when state changes
    citySelect.innerHTML = '<option selected disabled value="">Choose...</option>';
  } catch (error) {
    console.error('Error fetching states:', error);
    // Handle error 
  }
}

// Function to fetch and populate cities based on selected state
async function fetchCities() {
  const selectedCountry = countrySelect.value;
  const selectedState = stateSelect.value;

  try {
    const response = await fetch(`https://www.universal-tutorial.com/api/cities/${selectedCountry}/${selectedState}`, {
      headers: {
        "Accept": "application/json",
        "api-token": API_TOKEN,
        "user-email": "nyarashbayev97@gmail.com"
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const cities = await response.json();
    populateDropdown(citySelect, cities, 'city_name');
  } catch (error) {
    console.error('Error fetching cities:', error);
    // Handle error 
  }
}

// Helper function to populate a dropdown
function populateDropdown(selectElement, data, valueProperty) {
  selectElement.innerHTML = '<option selected disabled value="">Choose...</option>';
  data.forEach(item => {
    const option = document.createElement("option");
    option.value = item[valueProperty];
    option.text = item[valueProperty];
    selectElement.add(option);
  });
}

// Event listeners
countrySelect.addEventListener("change", fetchStates);
stateSelect.addEventListener("change", fetchCities);
citySelect.addEventListener("change", fetchCities);

// Initial fetch of countries
fetchCountries();