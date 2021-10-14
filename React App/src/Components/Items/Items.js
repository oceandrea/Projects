import {useEffect, useState} from 'react';
import styles from './Items.module.css'
import Item from './Item';

const Items = () => {
    const [searchParam, setSearchParam] = useState('');
    const [data, setData] = useState([]);
    const [filteredData, setFilteredData] = useState([]);

    useEffect(() => {
        const getData = async () => {
//             const response = await fetch('https://react-app-4ee0b-default-rtdb.firebaseio.com/cats.json');
//             const respData = await response.json();
//             setData(respData);
            
            try {
                const response = await fetch('https://react-app-4ee0b-default-rtdb.firebaseio.com/cats.json');

                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.message)
                }

                const respData = await response.json();
                setData(respData);

            } catch (e) {
                return alert(e.message)
            }
        };
        getData();
    }, [])

    const onSearchChangeHandler = (event) => {
        setSearchParam(event.target.value);
    };

    useEffect(() => {
        const filteredItems = data.filter(item => item.name.toLowerCase().includes(searchParam.toLowerCase()) || item.description.toLowerCase().includes(searchParam.toLowerCase()));
        setFilteredData(filteredItems);
    }, [searchParam, data])

    const result = !filteredData ? data : filteredData.map(item => <Item key={item.name} name={item.name}
                                                                         image={item.image}
                                                                         description={item.description}/>)

    return (
        <main>
            <form className={styles.form}>
                <div className={styles.search}>
                    <label htmlFor="search">Search</label>
                    <input type="text" value={searchParam} onChange={onSearchChangeHandler}/>
                </div>
            </form>
            <ul className={styles.result}>
                {result.length > 0 ? result : ''}
            </ul>
        </main>
    );
};

export default Items;
