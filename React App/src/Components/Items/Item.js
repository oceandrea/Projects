import styles from './Item.module.css'

const Item = (props) => {
    return (
        <li className={styles.card}>
            <img alt={props.name} src={props.image}/>
            <div className={styles.info}>
                <h3>{props.name}</h3>
                <p>{props.description}</p>
            </div>
        </li>
    );
}

export default Item;