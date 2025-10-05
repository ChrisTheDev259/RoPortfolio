let product_grid = document.getElementById("Product-grid")

const createPortfolioBtn = document.getElementById('create-portfolio-btn');

function createPortfolio() {
    console.log("Creating portfolio...");
    let description = "This is my portfolio description";

    fetch('/api/market/create-portfolio', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "title": "My Portfolio",
            "username": "christoffer",
            "body":description
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        });
    
    }

function Load_Products(grid) {
    fetch('/api/market/product-grid')
        .then(response => response.json())
        .then(data => {
            // Ensure 'products' exists in the response
            if (!data) {
                console.error('No products found in the response');
                return;
            }

            // Iterate over the 'products' array
            data.forEach(product => {
                let productCard = document.createElement('div');
                productCard.className = 'product-card';

                productCard.innerHTML = `
                <div class="h-96 w-80 bg-gray-500 rounded-xl shadow-md relative">
                    <img src="static/${product.img}" class="justify-self-center w-full h-4/5 rounded-xl">
                    <h1 id="Title" class="text-center text-2xl font-bold text-white w-full h-1/4 absolute bottom-0 rounded-b-xl bg-gray-800 flex justify-center items-center">
                        ${product.name}
                    </h1>
                </div>
                `;   
                grid.appendChild(productCard);
            });
        })
        .catch(error => console.error('Error loading products:', error));
}
Load_Products(product_grid);

createPortfolioBtn.addEventListener('click', createPortfolio);