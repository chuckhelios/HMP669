/** 
* Authentication Service
* @namespace root.authentication.services
* @memberOf root.authentication
*/
(function(){
	'use strict';

	angular
		.module('root.authentication.services')
		.factory('Authentication', Authentication);

	Authentication.$inject = ['$base64',  '$http', '$cookieStore', '$rootScope', '$timeout'];

	/**
	* @name Authentication
	* @returns {Factory}
	* @namespace root.authentication.services.Authentication
	* @memberOf root.authentication.services
	*/
	function Authentication($base64, $http, $cookieStore, $rootScope, $timeout) {
		var result = {
    		isError: false,
    		msg: ''
    	};

		/**
		* @name Authentication
		* @desc The Factory to be returned
		* @memberOf root.authentication.services.Authentication
		*/
	    var Authentication = {
	      getAuthenticatedAccount: getAuthenticatedAccount,
	      isAuthenticated: isAuthenticated,
	      login: login,
	      logout: logout,
	      setAuthenticatedAccount: setAuthenticatedAccount,
	      unauthenticate: unauthenticate
	    };

	    return Authentication;

	    /**
	     * @name login
	     * @desc Try to log in with username `username` and password `password`
	     * @param {string} username The username entered by the user
	     * @param {string} password The password entered by the user
	     * @returns {Promise}
	     * @memberOf root.authentication.services.Authentication
	     */
	    function login(username, password, callback){
	    	return $http.post('/api/auth/login/',{
	    		username: username, password: password
	    	}).then(loginSuccessFn, loginErrorFn);

			/**
			* @name loginSuccessFn
			* @desc Set the authenticated account and redirect to index
			*/
	    	function loginSuccessFn(data, status, headers, config){
	    		var isSupperUser = data.data.is_staff
	    		Authentication.setAuthenticatedAccount(username, password, isSupperUser);
	    		callback(data);
	    		// window.location = '/';
						    	
	    	}

			/**
			* @name loginErrorFn
			* @desc Log "Epic failure!" to the console
			*/
			function loginErrorFn(data, status, headers, config) {
			console.error("Login Error!");
			callback(data);

			// $scope.IsLoginError = true;
			// $scope.alertmsg = data.message;

			}

		}

	    /**
	     * @name getAuthenticatedAccount
	     * @desc Return the currently authenticated account
	     * @returns {object|undefined} Account if authenticated, else `undefined`
	     * @memberOf root.authentication.services.Authentication
	     */
	    function getAuthenticatedAccount() {
	      if (!$cookieStore.get('globals')) {
	        return;

	      }
	      console.log($cookieStore.get('globals'));

	      // return JSON.parse($cookies.authenticatedAccount);
	    }

		/**
		* @name isAuthenticated
		* @desc Check if the current user is authenticated
		* @return {boolean} True is user is authenticated
		* @memeberOf root.authentication.serivece.Authentication
		*/
		function isAuthenticated(){
			return $cookieStore.get('globals');
		}

		/**
		* @name setAuthenticatedAccount
		* @desc Stringify the account object to be stored
		* @return {undefined}
		* @memberOf root.authentication.service.Authentication
		*/
		function setAuthenticatedAccount(username, password, isSupperUser){
			var authdata = $base64.encode(username + ':' + password);
			$rootScope.globals = {
				currentUser: {
					username: username,
					isSupperUser: isSupperUser,
					authdata: authdata
				}
			};
            $http.defaults.headers.common['Authorization'] = 'Basic ' + authdata; // jshint ignore:line
            $cookieStore.put('globals', $rootScope.globals);
		}
		/**
		* @name unauthenticate
		* @desc Delete the cookie where the user object is stored
		* @returns {undefined}
		* @memberOf root.authentication.services.Authentication
		*/
		function unauthenticate() {
			$rootScope.globals = {};
			$cookieStore.remove('globals');
			$http.defaults.headers.common.Authorization = 'Basic ';
		}
	     /**
	     * @name logout
	     * @desc Try to log the user out
	     * @returns {Promise}
	     * @memberOf root.authentication.services.Authentication
	     */	
		function logout(callback) {
			return $http.post('/api/auth/logout/')
				.then(logoutSuccessFn, logoutErrorFn);

			/**
			* @name logoutSuccessFn
			* @desc Unauthenticate and redirect to index with page reload
			*/
			function logoutSuccessFn(data, status, headers, config) {
				Authentication.unauthenticate();
				callback(data)
				window.location = '/';
			}

			/**
			* @name logoutErrorFn
			* @desc Log "Epic failure!" to the console
			*/
			function logoutErrorFn(data, status, headers, config) {
				console.error('Epic failure!');
				callback(data);

			}
		}



	}
})();