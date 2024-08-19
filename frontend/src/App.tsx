import { Routes, Route } from "react-router-dom";

// Layout
import Layout from "./components/shared/Layout";

// Pages
import HomePage from "./pages/LandingPage";
import WorkoutsPage from "./pages/WorkoutsPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<HomePage />} />
        <Route path="/workouts" element={<WorkoutsPage />} />
      </Route>
    </Routes>
  );
}

export default App;