import React from 'react';
import RecipeReviewCard from './card.jsx'; // Assuming the component is in the same directory

export default function CustomCards() {
  return (
    <div> 
      {/* First Recipe Review Card */}
      <RecipeReviewCard
        image="/public/assets/images/cards/card_1.png"
        title="Shrimp and Chorizo Paella"
        subheader="September 14, 2016"
        // Other props as needed  
      />

      {/* Second Recipe Review Card */}
      <RecipeReviewCard
        image="/public/assets/images/cards/card_1.png"
        title="Margherita Pizza"
        subheader="October 25, 2023"
        // Other props as needed
      />

      {/* ... more RecipeReviewCard instances ... */}
    </div>
  );
}