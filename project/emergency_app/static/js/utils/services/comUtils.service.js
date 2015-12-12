/**
* ComUtils
* @namespace root.utils.services.comUtils
*/
(function(){
	'use strict';

	angular
		.module('root.utils.services')
		.factory('ComUtils', ComUtils);

	/**
	* @namespace Snackbar
	*/
	function ComUtils(){

		/**
		* @name ComUtils
		* @desc The factory to be returned
    	* @memberOf root.utils.services.Snackbar
		*/
		var ComUtils = {
			findByKey: findByKey,
		}

		return ComUtils;
		/**
		* @name findByKey
		* @desc Util for finding an object by its 'id' property among an array
		* @param {list} a : list of objects
		* @param {string} keyName : name of the key
		* @param {string||INT} id : key
		* @return {object} key element
	    * @memberOf root.utils.services.Snackbar
		*/
		function findByKey(a, keyName, id){
			for(var i = 0; i < a.length; i++){
				if(a[i][keyName] == id){ return a[i]}
			}
			return null;
		}		


	}

})();