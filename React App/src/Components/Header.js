import styles from './Header.module.css'
import Button from './UI/Button';
import {signOut} from '../service/firebase';

const Header = (props) => {
    const displayName = props.user ? props.user.multiFactor.user.displayName : '';

    return (
        <header className={styles.header}>
            <nav className={styles.navigation}>
                <h1 className={styles['home-button']}>HappyCats</h1>
                {displayName ?
                    <div className={styles.username}>
                        <span>Welcome, {displayName}</span>
                        <Button onClick={signOut}>Logout</Button>
                    </div> : ''}

            </nav>
        </header>
    );
}

export default Header;