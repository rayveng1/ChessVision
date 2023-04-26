import React from "react";
import { Nav, NavLink, NavMenu }
	from "./NavbarElements";

const Navbar = () => {
return (
	<>
	<Nav>
		<NavMenu>
		<NavLink to="/home" activeStyle>
			Home
		</NavLink>
		<NavLink to="/page1" activeStyle>
			Page1
		</NavLink>
		<NavLink to="/page2" activeStyle>
			Page2
		</NavLink>
		<NavLink to="/page3" activeStyle>
			Page3
		</NavLink>
		</NavMenu>
	</Nav>
	</>
);
};

export default Navbar;