from stack import Stack
def main():
    print("This is running !")
    st= Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.pop()
    # st.push(4)
    # st.push(5)
    st.print_stack()

if __name__=="__main__":
    main()