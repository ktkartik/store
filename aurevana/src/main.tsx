import {useEffect,useRef} from 'react';
import {createRoot} from 'react-dom/client';
import {mountStorefront} from './main.js';
import './styles/main.css';
// The dependency-free storefront controller is shared with the standalone preview.
function App(){const container=useRef<HTMLDivElement>(null);useEffect(()=>{if(container.current)return mountStorefront(container.current)},[]);return <div ref={container}/>;}
createRoot(document.getElementById('app')!).render(<App/>);
