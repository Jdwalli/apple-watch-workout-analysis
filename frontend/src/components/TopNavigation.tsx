import React from "react";
import { Link } from "react-router-dom";
import { cn } from "@/lib/utils";
import { NavigationLinks } from "@/config/NavigationLinks";
import { NavigationLink } from "@/types/navigation_types";
import { useSelector } from "react-redux";
import { RootState } from "../redux/store";
import UploadButtonDialog from "./UploadButtonDialog";

const TopNavigation: React.FC = () => {
  return (
    <div className="hidden flex-col md:flex">
      <div className="border-b">
        <div className="flex h-16 items-center px-4">
          <h2 className="text-lg font-bold tracking-tight">
            Apple Watch Workouts
          </h2>
          <Navbar className="mx-6" />
          <div className="ml-auto flex items-center space-x-4">
            <UploadButtonDialog />
          </div>
        </div>
      </div>
    </div>
  );
};

function Navbar({ className, ...props }: React.HTMLAttributes<HTMLElement>) {
  const exportDataStatus = useSelector(
    (state: RootState) => state.exportDataStatus.exportDataStatus
  );

  return (
    <nav
      className={cn("flex items-center space-x-4 lg:space-x-6", className)}
      {...props}
    >
      <Link
        to="/"
        className="text-sm font-medium transition-colors hover:text-primary"
      >
        Home
      </Link>

      {NavigationLinks.map((navLink: NavigationLink) => {
        const isDisabled = navLink.title === "Workouts" && !exportDataStatus;

        return (
          <Link
            key={navLink.link}
            to={isDisabled ? "#" : navLink.link}
            className={`text-sm font-medium transition-colors ${
              isDisabled
                ? "text-gray-400 cursor-not-allowed"
                : "text-muted-foreground hover:text-primary"
            }`}
          >
            {navLink.title}
          </Link>
        );
      })}
    </nav>
  );
}

export default TopNavigation;
