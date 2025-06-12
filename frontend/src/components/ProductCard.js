import React from "react"; // Importing React to define the component

// displays its name, description, and price
const ProductCard = ({ product }) => (
  <div className="product-card"> {/* Container for each product card */}
    <h4>{product.name}</h4> {/* Displays the product name */}
    <p>{product.description}</p> {/* Displays the product description */}
    <p className="price">Price: ₹{product.price}</p> {/* Displays product price */}
  </div>
);

// Exporting productcard components so to used in other parts of the app
export default ProductCard;
