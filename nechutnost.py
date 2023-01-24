class ModelNameListView(APIView):
    def get(self, request, model_name, *args, **kwargs):
        '''
        Return a response with all objects of model_name
        '''

        # Dynamically initialize vars with appropriate model name
        # Alternative is a big dict or a big match (switch) statement
        initialization = """
data = {mn}.objects
serializer = {mn}Serializer(data, many=True)
        """.format(mn=model_name)
        exec(initialization)

        return Response(serializer.data, status=status.HTTP_200_OK)


