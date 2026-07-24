import { Link } from "react-router-dom";

function Header() {
  return (
    <header className="bg-white shadow-sm">

      <div className="max-w-7xl mx-auto flex items-center justify-between px-6 py-4">

        <Link to="/" className="text-2xl font-bold text-blue-600">
          🛍 ShopWise AI
        </Link>

        <nav>

          <Link
            to="/"
            className="text-slate-600 hover:text-blue-600"
          >
            Home
          </Link>

        </nav>

      </div>

    </header>
  );
}

export default Header;