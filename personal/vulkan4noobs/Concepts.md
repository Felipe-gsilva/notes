```Markdown
## App struct or class
  This holds info on glfw window pointer and on the vulkan instance "object" itself, it works as an abstraction for the application.

## Window handler
  Glfw functions, such as `glfwInit`, `glfwWindowHint` and `glfwCreateWindow` (which returns a pointer to the window created). But you can literally use anything you want, like X11, Raylib or Win32.

## Instance
  Instances are vulkan subsystems which link the Vulkan libs and the application. Vulkan does not have a global state, so all tracked state must be stored somewhere. This memory region is the `vkInstance` object. Each instance will be soon "inserted" with a bunch of logical devices depending on each function you do implement. The `VkInstanceCreateInfo` function creates a bunch of info inside this object (being treated as a struct in this C code) which describes the vulkan instance with .sType(type of struct), with .pNext(point to next) and so on.

## Validation Layers (Optional for basic codes)
Validation layers are the debug layer you, dev, can add to the application. The vulkan docs adds lots of states you can share into your application and you can limit when this code run on the main header file.
  -Checking the values of parameters against the specification to detect misuse
  -Tracking creation and destruction of objects to find resource leaks
  -Checking thread safety by tracking the threads that calls originate from
  -Logging every call and its parameters to the standard output
  -Tracing Vulkan calls for profiling and replaying

## Physical devices and queues families
  VkPhysical Devices functiuons can handle the number of devices and the physical device properties and features.
  It is important to get all gpu properties and features with `vkGetPhysicalDeviceFeatures` or `vkGetPhysicalDeviceProperties` and store this info, so you can pass it to the application later on.

## Logical devices
  This are the Vulkan Abstraction for the Physical Devices handled before, they will be used in the future as the keepholders of important application info, such as the position where to render things and the gpu info gathered before.

## Queues
	You may recognize this structure from your algorythims classes. If you are not familiarized with this, I recommend you to study it before continuing. However, the absctraction is pretty much done and you won't need to have a profound knowledge about this subject.
// TODO

## Queues Families
  There are different types of queues that originate from different queue families and each family of queues allows only a subset of commands. For example, there could be a queue family that only allows processing of compute commands or one that only allows memory transfer related commands.

## Window surface
	A window surface is the vulkan representation of where to render on your screen. Vulkan is an agnostic API, sou it doesn't know where to render and furthermore, it doesn't care which lib you are using for your window managment.
	For that purpose, it uses the WSI (Window System Integration) to limit the area for rendering. You can use `VkSurfaceKHR` for GLFW.

## Swap Chain
	

## Image Views


## Dynamic states

## Vertex input

## Vertex Buffer

## Input assembly

## Viewport
	Adjust the pixels shown on the screen, adapting and resizing where they should be outputed. 

## Scissors
	Just cut the pixels outside some range or ratio you choose, so they are not rasterized and printed later on.

## Rasterizer

## Multisampling

## Depth and stencil testing

## Color blending

## Render Pass

## Render subpasses

## Recreating the Swap Chain
```