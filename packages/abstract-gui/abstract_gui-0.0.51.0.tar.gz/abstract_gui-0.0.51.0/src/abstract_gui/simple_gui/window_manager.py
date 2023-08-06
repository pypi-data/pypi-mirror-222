from .__init__ import sg,get_gui_fun
class WindowManager:
    """
    A class to manage PySimpleGUI windows and their events.

    Attributes:
        all_windows (dict): A dictionary to store registered windows along with their details.
        last_window (str): The name of the last accessed window.
        script_name (str): The name of the script that is using the WindowManager.
        global_bridge: The global bridge to access shared variables between different scripts.
        global_vars (dict): A dictionary to store global variables for this script.

    Methods:
        __init__(self, script_name, global_bridge):
            Initializes the WindowManager with the script name and global bridge.

        win_closed(self, event=''):
            Checks if the given event corresponds to a window close event.

        t_or_f_obj_eq(self, event=None, obj=None):
            Compares two objects and returns True if they are equal, False otherwise.

        verify_window(self, win: any = None) -> bool:
            Verifies if the given object is a valid PySimpleGUI window.

        close_window(self, win: any = None):
            Closes the given PySimpleGUI window.

        update_last_window(self, window):
            Updates the last accessed window to the given window.

        read_window(self, window):
            Reads the event and values from the given window and updates the WindowManager's state.

        get_event(self, window=None) -> Union[str, None]:
            Returns the last event of the specified window or the last accessed window.

        get_values(self, window=None) -> Union[Dict, None]:
            Returns the values of the specified window or the last accessed window.

        while_basic(self, window=None):
            Executes an event loop for the specified window or the last accessed window.

        delete_from_list(self, _list: List, var) -> List:
            Removes occurrences of a variable from a list and returns the new list.

        get_all_windows(self) -> Dict:
            Returns a dictionary containing all registered windows and their details.

        get_window_names(self) -> List[str]:
            Returns a list of names of all registered windows.

        is_window_object(self, obj) -> bool:
            Checks if the given object is a valid PySimpleGUI window object.

        create_window_name(self) -> str:
            Generates a unique name for a new window.

        get_window(self, win_name='', layout=None, args=None) -> sg.Window:
            Creates and returns a new PySimpleGUI window.

        register_window(self, obj=None) -> str:
            Registers a window object or creates a new window if no object is provided.

        search_global_windows(self, window) -> Union[str, bool]:
            Searches for a window in the global_vars dictionary and returns its name or False if not found.

        unregister_window(self, window):
            Unregisters a window and removes it from the global_vars and all_windows dictionaries.

        get_new_window(self, title="window", layout=None, args=None, event_function=None) -> sg.Window:
            Creates a new window with the given title, layout, and event function.
    """
    def __init__(self, script_name, global_bridge):
        """
        Initialize a WindowManager instance.

        Args:
            script_name (str): The name of the script that is using the WindowManager.
            global_bridge (GlobalBridge): An instance of GlobalBridge to access shared variables between different scripts.
        """
        self.all_windows = {'last_window': None}
        self.script_name = script_name
        self.global_bridge = global_bridge
        self.global_vars = self.global_bridge.return_global_variables(self.script_name)
        if "all_windows" in self.global_vars:
            self.all_windows = self.global_vars["all_windows"]
        self.global_vars["all_windows"] = self.all_windows
    def verify_args(self, args=None, layout=None, title=None, event_function=None):
        args = args or {}
        layout = layout or [[]]
        title = title or 'window'
        args.setdefault("title", title)
        args.setdefault("layout", layout)
        args.setdefault("event_function", event_function)
        return args
    def get_all_windows(self):
        """
        Get all registered windows.

        Returns:
            dict: A dictionary containing all registered windows and their details.
        """
        return self.all_windows
    def get_window_names(self):
        """
        Get the names of all registered windows.

        Returns:
            list: A list of names of all registered windows.
        """
        return self.delete_from_list(list(self.get_all_windows().keys()), 'last_window')
    def register_window(self, window=None):
        """
        Register a window.

        Args:
            obj (any, optional): The window to register. If not provided, a new window is created.

        Returns:
            str: The name of the registered window.
        """
        if window in self.get_window_names():
            name = window
        if self.is_window_object(window):
            name = self.search_global_windows(window)
            if name is False:
                name = self.create_window_name()
            self.all_windows[name] = {"method": window,"title":None,"closed":False, "values": {}, "event": "", "event_function": None}
            self.all_windows[name]["closed"]=False
        if window == None:
            name = self.create_window_name()
            self.all_windows[name] = {"method": None,"title":None,"closed":False, "values": {}, "event": "", "event_function": None}
        return name
    def get_window(self, title=None, layout=None, args=None):
        """
        Get a PySimpleGUI window.

        Args:
            win_name (str, optional): The name of the window. If not provided, a unique name is generated.
            layout (list, optional): The layout of the window. If not provided, an empty layout is used.
            args (dict, optional): Additional arguments for the window.

        Returns:
            any: A PySimpleGUI window.
        """
        args = self.verify_args(args, layout, title)
        return get_gui_fun('Window', {**args})
    def get_new_window(self, title=None, layout=None, args=None, event_function=None):
        """
        Create a new window.

        Args:
            title (str, optional): The title of the window. If not provided, 'window' is used.
            layout (list, optional): The layout of the window. If not provided, an empty layout is used.
            args (dict, optional): Additional arguments for the window.
            event_function (str, optional): The event function for the window.

        Returns:
            any: A new PySimpleGUI window.
        """
        args = self.verify_args(args=args, layout=layout, title=title, event_function=event_function)
        name = self.register_window()
        self.all_windows[name]["method"] = self.get_window(title=title, layout=layout, args=args)
        self.all_windows[name]["event_function"] = args["event_function"]
        self.all_windows[name]["title"] = title
        return self.all_windows[name]["method"]
    def search_global_windows(self, window):
        """
        Search for a window in the global variables.

        Args:
            window (any): The window to search for.

        Returns:
            any: The name of the window if found, False otherwise.
        """
        window_names = self.get_window_names()
        if self.is_window_object(window):
            for name in window_names:
                if self.all_windows[name]["method"] == window:
                    return name
        elif window in window_names:
            name = window
            return self.all_windows[window]["method"]
        return False
    def verify_window(self, window=None) -> bool:
        """
        Verifies if the given object is a valid PySimpleGUI window.

        Args:
            win (any): The object to verify.

        Returns:
            bool: True if the object is a valid window, False otherwise.
        """
        return self.search_global_windows(window=window) != False
    def update_last_window(self, window):
        """
        Update the last accessed window.

        Args:
            window (any): The window to set as the last accessed window.
        """
        name = window
        if self.is_window_object(window):
            name = self.search_global_windows(window)
            if name is False:
                name = self.register_window(window)
        if name in self.get_window_names():
            self.all_windows['last_window'] = name
    def send_to_bridge(self):
        self.global_vars["all_windows"] = self.all_windows
        self.global_bridge.retrieve_global_variables(self.script_name, self.global_vars)
    def close_window(self, window=None):
        """
        Closes the given PySimpleGUI window.

        Args:
            win (any): The window to close.
        """
        if self.verify_window(window):
            self.update_last_window(window)
            self.all_windows[self.search_global_windows(window)]["closed"] = True
            self.send_to_bridge()
            window.close()
    def read_window(self, window):
        """
        Read the event and values from a window and update the WindowManager's state.

        Args:
            window (any): The window to read from.
        """
        name = self.create_window_name()
        if self.is_window_object(window):
            name = self.search_global_windows(window)
            if name is False:
                name = self.register_window(window)
        if name not in self.get_window_names():
            return False
        window = self.all_windows[name]["method"]
        event, values = window.read()
        if event == sg.WIN_CLOSED and self.all_windows[name]["closed"] == False:
            self.all_windows[name]["closed"] = True
            self.all_windows[name]["event"] = 'EXIT'
            return 
        self.all_windows[name]["event"] = event
        self.all_windows[name]["values"] = values
        self.update_last_window(window)

    def get_event(self, window=None):
        """
        Get the last event from a window.

        Args:
            win (any, optional): The window to get the event from. If not provided, the last accessed window is used.

        Returns:
            any: The last event from the window.
        """
        if window is None:
            return self.all_windows[self.all_windows['last_window']]['event']
        name = self.search_global_windows(window)
        if name is not False:
            return self.all_windows[self.search_global_windows(window)]['event']

    def get_values(self, window=None):
        """
        Get the values from a window.

        Args:
            win (any, optional): The window to get the values from. If not provided, the last accessed window is used.

        Returns:
            dict: The values from the window.
        """
        if window is None:
            return self.all_windows[self.all_windows['last_window']]['values']
        name = self.search_global_windows(window)
        if name is not False:
            return self.all_windows[self.search_global_windows(window)]['values']

    def while_basic(self, window=None):
        """
        Run an event loop for a window.

        Args:
            window (any, optional): The window to run the event loop for. If not provided, the last accessed window is used.
        """
        self.global_vars = self.global_bridge.return_global_variables(self.script_name)
        input([self.verify_window(window),self.all_windows])
        while self.verify_window(window):
            self.read_window(window)
            if self.win_closed(self.get_event(window)):
                self.close_window(window)
                return self.all_windows[self.search_global_windows(window)]["values"]  # Return the stored data instead of all_windows
            event_function = self.all_windows[self.search_global_windows(window)]["event_function"]

            if event_function is not None:
                self.global_vars[event_function](self.get_event(window))
        self.close_window(window)
        return self.all_windows  # Return the stored data instead of all_windows
    def get_window_name(self, obj=None):
        """
        Get the names of all registered windows.

        Returns:
            list: A list of names of all registered windows.
        """
        window_names = self.get_window_names()
        if obj in window_names:
            name = obj
        if self.is_window_object(obj):
            name = self.search_global_windows(obj)
            if name is False:
                name = self.create_window_name()
        return name
    def win_closed(self, event=''):
        """
        Check if a window event calls to close the window.

        Args:
            event (str): The event to check.

        Returns:
            bool: True if the window is closed, False otherwise.
        """
        obj_ls = ["exit", "Exit", "EXIT", sg.WIN_CLOSED]
        return any(event == obj for obj in obj_ls)
    def delete_from_list(self, _list, var):
        return [each for each in _list if each != var]
    def is_window_object(self, obj):
        """
        Check if an object is a PySimpleGUI window object.

        Args:
            obj (any): The object to check.

        Returns:
            bool: True if the object is a window object, False otherwise.
        """
        return isinstance(obj, type(self.get_window()))
    def create_window_name(self):
        """
        Create a unique name for a window.

        Returns:
            str: A unique name for a window.
        """
        window_names = self.get_window_names()
        i = 0
        while 'win_' + str(i) in window_names:
            i += 1
        return 'win_' + str(i)
    def unregister_window(self, window):
        """
        Unregister a window.

        Args:
            window (any): The window to unregister.
        """
        win = self.search_global_windows(window)
        if win in self.get_window_names():
            del self.global_vars[win]
            del self.all_windows[win]
        elif self.is_window_object(win):
            del self.global_vars[window]
            del self.all_windows[window]
