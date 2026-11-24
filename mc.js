// const searchBtn = document.querySelector("button");

// searchBtn.addEventListener("click", () => {
//   const inputName = document.getElementById('searchName').value.toLowerCase();

//   fetch(`https://rickandmortyapi.com/api/character/?name=${inputName}`)
//     .then(response => response.json())
//     .then(data => {
//       const character = data.results[0];

//       document.getElementById("characterName").textContent = character.name;
//       document.getElementById("characterImage").src = character.image;
//     })
//     .catch(error => console.log("The Error is :", error));
// });


// const searchBtn = document.getElementById("searchBtn")


// searchBtn.addEventListener('click', () => {
//     const inputName = document.getElementById("searchName").value.toLowerCase()

//     fetch(`https://rickandmortyapi.com/api/location/?name=${inputName}`)
//     .then(response => response.json())
//     .then(data => {
//         const location = data.results[0]

//         document.getElementById("locationName").textContent = "Name: " + location.name
//         document.getElementById("locationType").textContent = "Type: " + location.type
//         document.getElementById("locationDimension").textContent = "Dimension: " +  location.dimension
//         document.getElementById("locationCount").textContent = "Count: " + location.count
//     })

// })



const buttons = document.querySelectorAll("button");
const container = document.getElementById("resultsContainer");

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const type = button.dataset.type; // "character", "location", or "episode"
    const inputName = document.getElementById('searchName').value.toLowerCase();

    fetch(`https://rickandmortyapi.com/api/${type}/?name=${inputName}`)
      .then(response => {
        if (!response.ok) {
          throw new Error(`No ${type} results found`);
        }
        return response.json();
      })
      .then(data => {
        renderResults(data.results, type);
      })
      .catch(error => {
        container.innerHTML = `<p>${error.message}</p>`;
        console.log("The Error is:", error);
      });
  });
});

function renderResults(results, type) {
  container.innerHTML = ""; // clear previous results

  results.forEach(item => {
    const div = document.createElement("div");

    if (type === "character") {
      div.innerHTML = `
        <h3>${item.name}</h3>
        <img src="${item.image}" width="100">
        <p>Status: ${item.status}</p>
        <p>Species: ${item.species}</p>
        <hr>
      `;
    } else if (type === "location") {
      div.innerHTML = `
        <h3>${item.name}</h3>
        <p>Type: ${item.type}</p>
        <p>Dimension: ${item.dimension}</p>
        <p>Residents: ${item.residents.length}</p>
        <hr>
      `;
    } else if (type === "episode") {
      div.innerHTML = `
        <h3>${item.name}</h3>
        <p>Episode: ${item.episode}</p>
        <p>Air date: ${item.air_date}</p>
        <p>Characters in episode: ${item.characters.length}</p>
        <hr>
      `;
    }

    container.appendChild(div);
  });
}