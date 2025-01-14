import { Link } from 'react-router-dom';

function Navigation() {
    return (
        <nav className="flex justify-between w-auto border-t-2 border-blue-700">
            <Link to="/search" >Search</Link>
            <Link to="/profile" >Profile</Link>
            <Link to="/campaigns" >Campaigns</Link>
            <Link to="/stats" >Stats</Link>
            <Link to="/support" >Support</Link>
        </nav>
    );
}

export default Navigation;