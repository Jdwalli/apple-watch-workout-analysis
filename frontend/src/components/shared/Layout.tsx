import React from "react";
import { Outlet } from "react-router-dom";
import TopNavigation from "../TopNavigation";

const Layout: React.FC = () => {
  return (
    <div className="h-screen w-screen flex flex-row">
      <div className="flex flex-col flex-1">
        <TopNavigation />
        <div className="flex-1 bg-background min-h-0 overflow-auto">
          <Outlet />
        </div>
      </div>
    </div>
  );
};

export default Layout;
