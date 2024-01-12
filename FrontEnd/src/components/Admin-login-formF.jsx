import '../index.css'
import React, { Component } from 'react';
import { FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import { faShieldHalved} from '@fortawesome/free-solid-svg-icons'
import { faEnvelope , faUser} from '@fortawesome/free-regular-svg-icons'

const AdminLoginF = () => {
    return (
            <div  className={'ml-16 mt-16'}>
                <div>
                    <FontAwesomeIcon className={''} icon={faUser}/>
                    <input className='w-[530px] h-[64px] border-2 ml-2 rounded-[16px] pl-4'
                           placeholder="Username" type="text"/>
                </div>
                <div className={'mt-4'}>
                    <FontAwesomeIcon icon={faShieldHalved}/>
                    <input className='w-[530px] h-[64px] border-2 ml-2 rounded-[16px] pl-4'
                           placeholder="Password" type="text"/>
                    {/*<FontAwesomeIcon icon={faEnvelope} />*/}
                </div>
                <div className={'w-[531px] h-[82px] mt-20 ml-[20px] bg-black rounded-3xl cursor-pointer'}>
                    <p className={'text-center text-white text-4xl pt-4'}>Login</p>
                </div>
                <p className={'text-2xl font-bold text-blue-300 ml-48 mt-6 cursor-pointer hover:text-blue-500 inline-block'}>Reset password</p>
                <p className={'font-bold text-3xl mt-2 ml-40 text-[#BCBCBC] inline-block'}>No accout?</p>
                <p className={'inline-block text-2xl font-bold text-blue-300 mt-5 ml-1 cursor-pointer hover:text-blue-500'}>create one</p>
                {/*<FontAwesomeIcon icon={faEnvelope} />*/}
        </div>

    )
        ;
}

export default AdminLoginF;