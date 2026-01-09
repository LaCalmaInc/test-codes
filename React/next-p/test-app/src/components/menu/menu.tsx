import Link from 'next/link';
import s from './menu.module.css';
import { Separator } from '@base-ui/react/separator';
const Menu = () =>{
    const menuItems = [
        {key: 'home', label: 'Home', href: '/'},
        {key: 'about-me', label: 'About me', href: '/about-me'},
    ];
    return (
        <div className={s.menu}>
            <Separator orientation="vertical" className={s.Separator}  />
            {menuItems.map((item) => (
                <Link key={item.key} href={item.href}>{item.label}</Link>
            ))}
        </div>
    );
};

export default Menu;