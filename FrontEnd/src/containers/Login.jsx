import '../index.css'
import AdminLoginF from '../components/Admin-login-formF';
const Login = () => {
    return ( 
        <>
            <div className={'w-[720px] h-[600px] bg-[#F2F2F2] mx-auto my-auto mt-20 rounded-[32px]'}>
                <p className={'text-5xl text-center pt-8'}>Admin Login</p>
                <AdminLoginF />
            </div>
        </>
     );
}
 
export default Login;