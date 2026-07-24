const API_URL = import.meta.env.VITE_API_URL;

async function request(path, options = {}) {
    const response = await fetch(`${API_URL}${path}`, {
        headers: {
            "Content-Type": "application/json",
        },
        ...options,
    });

    if (!response.ok) {
        throw new Error(await response.text());
    }

    return response.json();
}

export async function getProducts(category = "") {
    const url = category
        ? `/api/products?category=${encodeURIComponent(category)}`
        : "/api/products";

    const result = await request(url);

    return result.data;
}

export async function getCategories() {
    const result = await request("/api/categories");
    return result.data;
}

export async function getProduct(id) {
    const result = await request(`/api/products/${id}`);
    return result.data;
}

export async function recommend(productId) {
    return request("/api/recommend", {
        method: "POST",
        body: JSON.stringify({
            product_id: productId,
        }),
    });
}