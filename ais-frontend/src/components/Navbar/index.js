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
			Confirm
		</NavLink>
		<NavLink to="/Results" activeStyle>
			Results
		</NavLink>
		</NavMenu>
	</Nav>
	</>
);
};

export default Navbar;