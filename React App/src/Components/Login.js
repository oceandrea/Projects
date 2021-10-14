import Button from './UI/Button';
import styles from './Login.module.css'
import {signInWithGoogle} from '../service/firebase';

const Login = () => {
    return (
        <main className={styles['login-container']}>
            <Button onClick={signInWithGoogle} className={styles['login-button']}>
                Login
            </Button>
        </main>

    );
}

export default Login;