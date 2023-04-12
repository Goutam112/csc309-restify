import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import MyRentalUnits from './pages/MyRentalUnits/MyRentalUnits';
import CreateProperty from './pages/CreateProperty/CreateProperty'

const root = ReactDOM.createRoot(document.getElementById('root'));

let authorizationToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxMzMwNjY1LCJpYXQiOjE2ODEyNDQyNjUsImp0aSI6Ijk1ZTQ1Yjc1NGQyODQ5NjE5NWQ0NzUxMzI4N2EzYTg5IiwidXNlcl9pZCI6Mn0.OOO919b4GRTxAsQmDwb4wea3u4XuAc45qHT4EOfaiLg";

localStorage.setItem('authorizationToken', `Bearer ${authorizationToken}`);


root.render(
  <React.StrictMode>
    <App />
    {/* <MyRentalUnits /> */}
    {/* <CreateProperty></CreateProperty> */}
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
