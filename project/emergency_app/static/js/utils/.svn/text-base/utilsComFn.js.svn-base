

Object.defineProperty(
    Object.prototype, 
    'renameProperty',
    {
        writable : false, // Cannot alter this property
        enumerable : false, // Will not show up in a for-in loop.
        configurable : false, // Cannot be deleted via the delete operator
        value : function (oldName, newName) {
            // Do nothing if the names are the same
            if (oldName == newName) {
                return this;
            }
            // Check for the old property name to 
            // avoid a ReferenceError in strict mode.
            if (this.hasOwnProperty(oldName)) {
                this[newName] = this[oldName];
                delete this[oldName];
            }
            return this;
        }
    }
);


  /**
  * @name getFormatDate
  * @param {object} dateRange : object that contain date
  * @param {string} dir : from/to
  * @desc formate date to  yyyy-mm-dd string
  * @memberOf fcny.layout.controllers.DatePickerController
  */
  function getFormatDate(date, dir){
    var day = date[dir].getDay();
    var mon = date[dir].getMonth();
    var year = date[dir].getFullYear();
    var date = year + '-' + mon + '-' + day;
    return date;
  } 