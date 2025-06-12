// Importing the axios library for making HTTP requests
import axios from "axios";

/**
 * Function to search for products
 
  @param {string} query - search input for user 
  @returns {Promise<Array>} - array matching to products
 */
export const searchProducts = async (query) => {
  // making a request to flask API 
  const res = await axios.get(`http://localhost:5000/api/products?q=${query}`);

  // Return the product data from the response
  return res.data;
};
