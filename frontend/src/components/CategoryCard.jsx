import { Link } from "react-router-dom";

function CategoryCard({ category }) {
  return (
    <Link to={`/category/${category.id}`}>
      <div
        style={{
          border: "1px solid #ddd",
          borderRadius: 10,
          padding: 20,
          background: "white",
          transition: "0.2s",
        }}
      >
        <h2>{category.title}</h2>

        <p
          style={{
            marginTop: 10,
            color: "#666",
          }}
        >
          {category.description}
        </p>
      </div>
    </Link>
  );
}

export default CategoryCard;