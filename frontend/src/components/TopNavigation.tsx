import React from "react";
import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";
import { cn } from "@/lib/utils";
import { NavigationLinks } from "@/config/NavigationLinks";
import { NavigationLink } from "@/types/navigation_types";

const TopNavigation: React.FC = () => {
  return (
    <div className="hidden flex-col md:flex">
      <div className="border-b">
        <div className="flex h-16 items-center px-4">
          <h2 className="text-lg font-bold tracking-tight">
            Apple Watch Dashboard
          </h2>
          <Navbar className="mx-6" />
          <div className="ml-auto flex items-center space-x-4">
            <Button>Upload</Button>
          </div>
        </div>
      </div>
    </div>
  );
};

function Navbar({ className, ...props }: React.HTMLAttributes<HTMLElement>) {
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

      {NavigationLinks.map((navLink: NavigationLink) => (
        <Link
          key={navLink.link}
          to={navLink.link}
          className="text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
        >
          {navLink.title}
        </Link>
      ))}
    </nav>
  );
}

export default TopNavigation;
