import React from "react";
import { ThemeProvider } from "@/components/theme-provider";
import Layout from "./components/shared/Layout";
import { Routes, Route } from "react-router-dom";

// Pages
import LandingPage from "./pages/landing/LandingPage";
import WorkoutsPage from "./pages/workouts/WorkoutsPage";

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<LandingPage />} />
          <Route path="/workouts" element={<WorkoutsPage />} />
        </Route>
      </Routes>
    </ThemeProvider>
  );
}

export default App;
