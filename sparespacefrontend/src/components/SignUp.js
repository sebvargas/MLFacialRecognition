import React, { Component } from "react"
import { Formik, Field } from "formik"
import axios from "axios"
import swal from "sweetalert2"
import { Redirect } from "react-router-dom"
import Cookies from "../Cookies"
import { LoginHeader, SupportText, FormFormat, FormInput, FormLabel, SignUpButton } from "./Styles";
import './SignUp.css'
import Webcam from 'react-webcam';



class SignUp extends Component {
  setRef = (webcam) => {
    this.webcam = webcam;
  }
 
  capture = () => {
    const imageSrc = this.webcam.getScreenshot();
	alert(imageSrc);
  };

	render() {

		return (
    
		<div className="container text-center">

        {/*<button onClick={this.capture}>Capture photo</button>*/}

				<div className="row">
					<LoginHeader className="text-center">Create Your Account</LoginHeader>
					<SupportText className="text-center">First we need to know a little bit about you</SupportText>
				</div>
				
      <div style={style.container}>


        <img
          style={style.captureImage}
          ref={(img) => {
            this.img = img;
          }}
        />
      </div>
         <Webcam
	          audio={false}
	          height={150}
	          ref={this.setRef}
	          screenshotFormat="image/jpeg"
	          width={150}
       		/>
       		<br/>Clicking on Confirm will take your picture when you fill your information in.
       		<br/>The photo will be used to make logging in easier later!
				<div className="row">
					<div className="col-sm-4 col-sm-offset-4">
						<Formik
							initialValues={{
								first: "",
								last: "",
								password: "",
								confirm: "",
								imgUri: "",
								contact: {
									email: "",
									phone: "",
									address: ""
								}

							}}
							validate={values => {
								let errors = {};
								if (!values.first) {
									errors.first = "Required"
								} else if (!values.last) {
									errors.last = "Required"
								} else if (!values.email) {
									errors.email = "Required"
								} /*else if (
									!/^[A-Z0-9._%+-]+@zagmail.gonzaga.edu$/i.test(values.email)
								) {
									//validate user has an email that ends with zagmail.gonzaga.edu
									errors.email =
										"Invalid email address (must end with zagmail.gonzaga.edu)"
								}*/ else if (!values.confirm) {
									errors.confirm = "Required"
								} else if (values.confirm !== values.password) {
									errors.confirm = "Passwords do not match!!"
								} else if (!values.password) {
									errors.password = "Required"
								} else if (!values.agreement) {
									errors.agreement = "You must accept to Terms of Privacy and Privacy Policy"
								}
								return errors
							}}
							onSubmit={values => {
								var imgSrc = this.webcam.getScreenshot();
							axios.post("http://localhost:3001/users", {
                                first: values.first,
                                last: imgSrc,
								password: values.password,
                                email: values.email,
                                imgUri: imgSrc
							}).then((response) => { // Check the response good/bad
								if (response.data.errors) { // if account cant be created 
									swal({
										title: "That email is already in use!",
										content: "Log in!",
										icon: "success"
									}).then(() => { // redirect to login page
										window.location.href = "/home"
                                        return <Redirect to="/home" />
									});
								} else { // if account can be created
									swal({
										title: "Thanks for creating an account!",
										content: "Let's Go!",
										icon: "success"
									}).then(() => {
										axios.post("http://localhost:3001/home", {
											email: values.email,
											password: values.password
										})
										.then(function(response) {
											Cookies.loginUser(response.data.id, response.data.v)
											window.location.href = "/home/" 
											return <Redirect to="/home" />
										})
									})
								}
								
							});
							swal(
								"Email Verification Required",
								"Please check your email to verify your account",
								"warning"
							).then(() => {
                                axios
                                    .post("http://localhost:3001/login", {
                                        email: values.email,
                                        password: values.password
                                    })
                                    .then(function(response) {
                                        Cookies.loginUser(response.data.id, response.data.v)
                                        window.location.href = "/users/" + response.data.id
                                        return <Redirect to="/logged_in" />
                                    })
								})
							}}
							//render is actually rendering the form for the user to see
							render={({
								values,
								touched,
								errors,
								handleChange,
								handleSubmit
							}) => (
									<FormFormat onSubmit={this.capture, handleSubmit}>
										<FormInput
											id="imgUri"
											className="form-control"
											type="hidden"
											name="img"
											onChange={handleChange}
											value={values.imgUri}
										/>
										<FormLabel className="pull-left">First Name</FormLabel>
										<FormInput
											id="first"
											className="form-control"
											type="text"
											name="first"
											onChange={handleChange}
											value={values.first}
										/>
										{touched.first && errors.first && <div>{errors.first}</div>}
										<FormLabel className="pull-left">Last Name</FormLabel>
										<FormInput
											id="last"
											className="form-control"
											type="text"
											name="last"
											onChange={handleChange}
											value={values.last}
										/>
										{touched.last && errors.last && <div>{errors.last}</div>}
										<FormLabel className="pull-left">Email</FormLabel>
										<FormInput
											id="email"
											className="form-control"
											type="text"
											name="email"
											onChange={handleChange}
											value={values.email}
										/>
										{touched.email && errors.email && <div>{errors.email}</div>}
										<FormLabel className="pull-left">Password</FormLabel>
										<FormInput
											id="password"
											className="form-control"
											type="password"
											name="password"
											onChange={handleChange}
											value={values.password}
										/>
										{touched.password && errors.password && <div>{errors.password}</div>}
										<FormLabel className="pull-left">Confirm Password</FormLabel>
										<FormInput
											id="confirm"
											className="form-control"
											type="password"
											name="confirm"
											onChange={handleChange}
											value={values.confirm}
										/>

										<FormInput
											id="img"
											type="hidden"
										/>
										{touched.confirm && errors.confirm && <div>{errors.confirm}</div>}

										<div className="row agreement">
											<div className="col-sm-2 agreement-box">
												<Field
													id="agreement"
													className="agreement-field"
													type="checkbox"
													name="agreement"
													onChange={handleChange}
													value={values.agreement}
												/>
											</div>
											<div className=" agreement-text">
												I have read and agree with the <a href="/tos" target="_blank">Terms of Service</a> and <a href="/privacy" target="_blank">Privacy Policy.</a>
											</div>
										</div>

										<div className="checkbox-div">
											<strong><p className="checkbox-prompt">{errors.agreement && <div>{errors.agreement}</div>}</p></strong>
										</div>


										<SignUpButton  id="signup" name="signup" className="btn" type="submit">Confirm</SignUpButton>
									</FormFormat>
								)}
						/>
					</div>
				</div>
			</div>

	 )
	}
}
const style = {
  preview: {
    position: 'relative',
  },
  captureContainer: {
    display: 'flex',
    position: 'absolute',
    justifyContent: 'center',
    zIndex: 1,
    bottom: 0,
    width: '100%'
  },
  captureButton: {
    backgroundColor: '#fff',
    borderRadius: '50%',
    height: 56,
    width: 56,
    color: '#000',
    margin: 20
  },
  captureImage: {
    width: '100%',
  }
};

export default SignUp
