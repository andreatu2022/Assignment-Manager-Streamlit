# Review Presentation Outline: Common Pitfalls & Clarifications in Streamlit

## Slide 1: Streamlit Keys (The Most Common Trap)

- **The Duplicate Key Error**: Copying and pasting UI elements (like a select box) without changing the `key` argument will instantly crash the app. Every single input widget must have a strictly unique key identifier.

- **Static vs. Dynamic Keys**:
    - **Use Static Keys** (e.g., `key="edit_title"`) when you want the UI to remember what the user typed even if the page refreshes.
    - **Use Dynamic Keys** (e.g., `key=f"type_{assignment_edit['id']}"`) when the UI needs to completely reset and load fresh data, such as when switching between different assignments to edit.

## Slide 2: Page Reruns & Disappearing Feedback

- **The Outdated AI Suggestion**: AI coding assistants often suggest using `st.experimental_rerun()`. This code is outdated and broken; it must be written exactly as `st.rerun()` with parentheses.

- **The "Blink and You Miss It" Message**: If you trigger a success message (like `st.success`) immediately before a page rerun, the app refreshes so fast that the user never sees the message.

- **The Fix**: Always insert a pause using `time.sleep()` (e.g., for 4 or 5 seconds) before the rerun command so the user has time to read the visual feedback.

## Slide 3: Widget Quirks & Data Matching

- **Radio Buttons Work Differently**: Most input widgets accept a `value` argument to set their default state. However, `st.radio` does not; it requires an `index` argument (an integer representing the item's position in a list).

- **Case-Sensitivity Crashes**: When writing logic to automatically find that index number from text data, mismatched capitalization (e.g., "Homework" vs "homework") will cause the app to throw an error. Text data should always be normalized (using `.lower()` or `.capitalize()`) before attempting to match it.

## Slide 4: Behind-the-Scenes Coding Hiccups

- **The "Ghost" Variables**: It is incredibly easy to accidentally use a variable name from a previous lecture or entirely different function (e.g., typing `selected_assignment` instead of `assignment_edit`), which will cause the UI to load the wrong data.

- **Indentation is Unforgiving**: Streamlit heavily relies on `with` blocks (like `with st.expander:` or `with tab1:`). Missing a single indentation level will break the app's layout or cause a runtime error that can be difficult to spot during live development.

- **Python Version Quirks**: Different versions of Python across different laptops can sometimes handle syntax uniquely; for example, throwing an error over double quotes `""` versus single quotes `''`.

## Slide 5: Starting & Running the App (The Terminal Trap)

- **The Wrong Run Command**: You cannot run a Streamlit app by just pressing "Run Python File" or typing `python app.py`. It must be executed strictly through the terminal using the command `streamlit run app.py` (or whatever your filename is).

- **The "Connection Error" Panic**: If you accidentally close your VS Code terminal, your browser will show a "Connection Lost" error. Your app is not broken; you simply need to open a new terminal and type the `streamlit run` command again to restore the connection.

- **Variables are Mandatory**: When creating an input widget, you must store it in a variable (e.g., `title = st.text_input("Title")`). If you just write the `st.text_input` code without assigning it to a variable, the app will display the box, but you will have no way to capture or use the user's input later.

## Slide 6: Choosing the Right Widget (Design Pitfalls)

- **The Categorical Data Trap (Grade Deduction)**: Do not use `st.text_input` for data that has strict predefined categories (like choosing between "Homework" or "Lab"). Letting the user type freely when the options are limited is bad design; you must use `st.selectbox` or `st.radio` to force a valid choice.

- **Radio vs. Selectbox Rules**:
    - **Use `st.selectbox`** if the input is optional. You can include a "Select an option" choice so the user can leave it essentially blank.
    - **`st.radio`** forces a selection instantly and should not be used if the user is allowed to skip the question.

- **Long Text**: Never use `st.text_input` for long inputs like assignment descriptions. It restricts the user to a single line; always use `st.text_area` instead.

- **Action Triggers**: Never use a select box or radio button to execute a major action (like saving data or switching pages). Actions must strictly be triggered by an `st.button` click.

## Slide 7: Layout Polish & Container Rules

- **Placeholder vs. Help Arguments**:
    - **Use `placeholder`** for quick formatting hints; it disappears the moment the user starts typing.
    - **Use `help`** if you need to provide permanent context about why you are asking for the data. This creates a small question mark icon that the user can hover over at any time.

- **Proportional Columns**: Typing `st.columns(2)` creates two perfectly equal columns. If you want one column to be larger than the other, you must pass a list of proportions, such as `st.columns([2, 1])`, which makes the first column twice as wide as the second.

- **Container Indentation**: When using `with st.container():` or `with col1:`, every single element that belongs inside that area must be indented on the next line. If you miss the indentation, the element will "fall out" of the container and break your layout.