import React from 'react'



export default function SignIn() {

    const ShowPass = () => {
        let pass1 = document.getElementById('password');
        if ( pass1.type === 'password'){
            pass1.type = 'text';
        }
        else{
            pass1.type = 'password';
        }
    }

    // my style 
    let Mystyle = {
        borderRadius:'15px'
    }


    return (
        <>
            <div className='p-5' >
                <div className="container my-5 bg-light p-5   w-50 shadow" id='login-div' style={Mystyle}>

                    <form>
                        <div className="mb-3">
                            <label htmlFor="username" className="form-label">Email Username</label>
                            <input type="text" className="form-control" id="username" aria-describedby="usernameHelp" />

                        </div>

                        <div className="mb-3">
                            <label htmlFor="password" className="form-label">Enter Password</label>
                            <input type="password" className="form-control" id="password" />
                        </div>
                        <div className="mb-3 form-check">
                            <input type="checkbox" className="form-check-input" id="showpass" onClick={ShowPass} />
                            <label className="form-check-label" htmlFor="showpass">Show Password</label>
                        </div>
                        <button type="submit" className="btn btn-primary">Login</button>
                    </form>
                </div>
            </div>
        </>
    )
}
