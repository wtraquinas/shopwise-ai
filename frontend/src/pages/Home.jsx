import { useEffect, useState } from "react";

import api from "../services/api";

import Header from "../components/Header";
import Footer from "../components/Footer";
import Loading from "../components/Loading";
import CategoryCard from "../components/CategoryCard";

function Home() {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadProducts() {
      const data = await getProducts();
      setProducts(data);
    }

    loadProducts();
  }, []);

  return (
    <>
      <Header />

      <main
        style={{
          maxWidth: 1200,
          margin: "40px auto",
          padding: 20,
        }}
      >
        <h2>Choose a Category</h2>

        {loading ? (
          <Loading />
        ) : (
          <div
            style={{
              display: "grid",
              gap: 20,
              gridTemplateColumns:
                "repeat(auto-fit,minmax(250px,1fr))",
              marginTop: 30,
            }}
          >
            {categories.map((category) => (
              <CategoryCard
                key={category.id}
                category={category}
              />
            ))}
          </div>
        )}
      </main>

      <Footer />
    </>
  );
}

export default Home;