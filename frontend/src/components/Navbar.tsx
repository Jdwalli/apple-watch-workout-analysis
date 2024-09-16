import { Link } from "react-router-dom";
import { cn } from "@/lib/utils";
import { NavigationLinks } from "@/config/NavigationLinks";
import { NavigationLink } from "@/types/navigation_types";

export function Navbar({
  className,
  ...props
}: React.HTMLAttributes<HTMLElement>) {
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
