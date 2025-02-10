document.addEventListener('DOMContentLoaded', () => {
    /* Fun Fact Box Functionality */
    const facts = [
      "Did you know that shawarma originally comes from the Middle East and means 'turning'? The meat is cooked on a rotating spit!",
      "Kebabs are enjoyed worldwide, with various regional twists – from the Turkish döner to the Lebanese shawarma!",
      "The secret to a great kebab is in the marinade and spices – many chefs guard their recipes closely!",
      "Shawarma is often served with garlic sauce and pickles, adding a burst of flavor to every bite.",
      "In Denmark, kebab and shawarma joints have become popular social hubs, known for their vibrant atmospheres!"
    ];
  
    let currentFactIndex = 0;
    const factText = document.getElementById('fact-text');
    const nextFactButton = document.getElementById('next-fact');
  
    nextFactButton.addEventListener('click', () => {
      currentFactIndex = (currentFactIndex + 1) % facts.length;
      factText.textContent = facts[currentFactIndex];
    });
  });
  