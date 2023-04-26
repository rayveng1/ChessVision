import React from "react";
import { Nav, NavLink, NavMenu }
	from "./NavbarElements";

const Navbar = () => {
return (
	<>
	<Nav>
		<NavMenu>
		<NavLink to="/Main" activeStyle>
			Home
		</NavLink>
		<NavLink to="/Confirm" activeStyle>
			Page2
		</NavLink>
		<NavLink to="/Results" activeStyle>
			Page3
		</NavLink>
		</NavMenu>
	</Nav>
	</>
);
};

export default Navbar;