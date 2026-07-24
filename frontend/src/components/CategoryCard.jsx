import { Link } from "react-router-dom";

function CategoryCard({ category }) {
  return (
    <Link
      to={`/category/${category.id}`}
      style={{
        textDecoration: "none",
        color: "inherit",
      }}
    >
      <div
        style={{
          background: "#ffffff",
          border: "1px solid #e5e7eb",
          borderRadius: "16px",
          padding: "24px",
          height: "220px",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          transition: "0.2s ease",
          cursor: "pointer",
        }}
      >
        <div>
          <div
            style={{
              fontSize: "42px",
              marginBottom: "16px",
            }}
          >
            {category.icon}
          </div>

          <h2
            style={{
              margin: 0,
              marginBottom: "10px",
              fontSize: "28px",
            }}
          >
            {category.name}
          </h2>

          <p
            style={{
              color: "#64748b",
              lineHeight: 1.5,
            }}
          >
            {category.description}
          </p>
        </div>

        <div
          style={{
            color: "#2563eb",
            fontWeight: "bold",
          }}
        >
          Browse →
        </div>
      </div>
    </Link>
  );
}

export default CategoryCard;