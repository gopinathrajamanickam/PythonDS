class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        return (self.head_node is None)

    def insert_at_head(self, data):
        new_element = Node(data)
        new_element.next_element = self.head_node
        self.head_node = new_element

    def insert_at_tail(self, data):
        new_element = Node(data)
        if self.get_head() is None:
            self.head_node = new_element
        else:
            curr_element = self.get_head()
            while(curr_element.next_element is not None):
                curr_element = curr_element.next_element
            curr_element.next_element = new_element

    def insert_at_pos(self, data, pos):

        # if list is empty exit
        if self.is_empty():
            print('List is empty')
            return

        # Traverse to the insertion position
        curr_pos = 1
        curr_element = self.get_head()
        while (curr_element.next_element is not None and curr_pos < pos - 1):
            print(curr_pos, curr_element.data)
            curr_pos += 1
            curr_element = curr_element.next_element

        if (curr_element.next_element is not None):
            # create a new_node
            new_element = Node(data)

            # point the new_node.next as curr_node.next
            new_element.next_element = curr_element.next_element

            # point curr_node.next as new_node
            curr_element.next_element = new_element

    def search(self, value):
        if self.is_empty():
            print('List is empty')
            return

        curr_pos = 1
        curr_node = self.get_head()
        while (curr_node.next_element is not None):
            if curr_node.data == value:
                print('Value {0} is at position {1}'.format(value, curr_pos))
                return
            else:
                curr_pos += 1
                curr_node = curr_node.next_element

    def delete_at_head(self):
        # get the first node
        # mark the second node as head node
        if self.is_empty():
            print('List is empty')
        else:
            self.head_node = self.head_node.next_element

    def delete_at_tail(self):
        # Traverse to second last node
        if self.is_empty():
            print('List is empty')
        else:
            curr_node = self.get_head()
            prev_node = curr_node
            while(curr_node.next_element is not None):
                prev_node = curr_node
                curr_node = curr_node.next_element
            # mark the next element as None
            prev_node.next_element = None

    def delete_by_pos(self, pos):
        print('Inside Delete by position')
        # Traverse to the position
        if self.is_empty():
            print('List is empty')
        else:
            curr_node = self.get_head()
            curr_pos = 1
            prev_node = curr_node

            while (curr_node.next_element is not None and curr_pos <= pos):
                print('Current position : {0} with value {1}'.format(
                    curr_pos, curr_node.data))
                prev_node = curr_node
                curr_pos += 1
                curr_node = curr_node.next_element

            # prev_nodes next element to point to current elements next node
            prev_node.new_element = curr_node.next_element

    # def delete_by_value(self, value):
    #     # Traverse to the node of given value
    #     if self.is_empty():
    #         print('List is empty')
    #     else:
    #         curr_node = self.get_head()
    #         prev_node = curr_node
    #         while (curr_node.next_element is not None):
    #             if (curr_node.data == value):
    #                 # prev nodes next element to point to current element's next node
    #                 prev_node.next_element = curr_node.next_element
    #                 return
    #             print('Current value {0}'.format(curr_node.data))
    #             prev_node = curr_node
    #             curr_nodee = curr_node.next_element
    #         print('Given value {0} not found in the list'.format(value))

    def print_list(self):
        # check if list is empty
        if self.is_empty():
            print('List is Empty')
        else:
            curr_node = self.get_head()
            final_print = str(curr_node.data)
            while (curr_node.next_element is not None):
                curr_node = curr_node.next_element
                final_print += " -> " + str(curr_node.data)
            final_print += " -> None"
            print(final_print)


lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(2)
lst.insert_at_tail(3)
lst.insert_at_tail(4)
lst.insert_at_pos(5, 3)
lst.print_list()
lst.search(3)
lst.delete_at_head()
lst.print_list()
lst.delete_at_tail()
lst.print_list()

lst.delete_by_pos(2)
# lst.delete_by_value(3)
lst.print_list()
